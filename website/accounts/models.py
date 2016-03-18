from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class CustomuserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, id, password=None):
        '''
        Creates and saves a User with the given email, first name, last name, id
        and password.
        '''
    
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
                        email=self.normalize_email(email),
                        first_name=first_name,
                        last_name=last_name,
                        id=id,
                        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, id, password):
        '''
        Creates and saves a superuser with the given email, firstname, lastname
        , id and password
        '''

        user = self.create_user(
                                email, password=password, first_name=first_name,
                                last_name=last_name, id=id
                               )

        user.is_admin = True
        user.save(using=self._db)

        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
                              verbose_name='email_address',
                              max_length = 255,
                              unique=True
                             )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.CharField(max_length=8)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'id']

    def get_full_name(self):
        # Return the user's full name

        return self.first_name + " " + self.last_name

    def get_short_name(self):
        # Return the user's first name

        return self.first_name

    def __str__(self):
        # Return the user's email

      return self.email 

    def has_perm(self, perm, obj=None):
        # Does user have a specific permission"
        
        return True;

    @property
    def is_staff(self):
        
        return self.is_admin





