from django.http import HttpResponse
from django.template import Context, loader

def index(request):

    # Load the template
    template = loader.get_template('index.html') 

    return HttpResponse(template.render())
