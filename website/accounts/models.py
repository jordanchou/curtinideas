from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.template.defaultfilters import slugify

#-----------------------------------------------------------------------------

class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, sid, password=None, **args):
        '''
        Creates and saves a User with the given email, first name, last name, sid
        and password.
        '''

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
                        email=self.normalize_email(email),
                        first_name=first_name,
                        last_name=last_name,
                        sid=sid
                        )

        user.slug =(user.email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, sid, password, **args):
        '''
        Creates and saves a superuser with the given email, firstname, lastname
        , sid and password
        '''

        user = self.create_user(
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                sid=sid,
                                password=password
                               )

        user.is_admin = True
        user.save(using=self._db)

        return user

#-----------------------------------------------------------------------------

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
                              verbose_name='email address',
                              max_length = 255,
                              unique=True
                             )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sid = models.CharField(max_length=8, default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    slug = models.SlugField(max_length = 255, null = False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'sid']

    def get_full_name(self):
        # Return the user's full name

        return self.first_name + " " + self.last_name

    def get_short_name(self):
        # Return the user's first name

        return self.first_name

    def __str__(self):
        # Return the user's email

      return self.email

    def get_email(self):
        # Return the user's email

      return self.email

    def has_perm(self, perm, obj=None):
        # Does user have a specific permission"

        return True;

    @property
    def is_staff(self):

        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def authenticated(self):
        return True

    def voted_on(self, submission):
        voted_subs = ComVoting.objects.filter(voter=self, submission=submission)
        return voted_subs

#-----------------------------------------------------------------------------
