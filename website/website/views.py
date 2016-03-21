from django.http import HttpResponse
from django.template import Context, loader

def index(request):

    # Load the template
    template = loader.get_template('index.html') 

    return HttpResponse(template.render())

def about_us(request):
    # Load template
    template = loader.get_template("about_us.html")

    return HttpResponse(template.render())

def contact_us(request):
    # Load template
    template = loader.get_template("contact_us.html")

    return HttpResponse(template.render())

def faq(request):
    # Load template
    template = loader.get_template("faq.html")

    return HttpResponse(template.render())