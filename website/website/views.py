from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

def index(request):

    # Load the template
    template = loader.get_template('index.html') 

    return render(request, 'index.html', {})

def about_us(request):
    # Load template
    template = loader.get_template("about_us.html")

    return render(request, 'about_us.html', {})

def contact_us(request):
    # Load template
    template = loader.get_template("contact_us.html")

    return render(request, 'contact_us.html', {})

def faq(request):
    # Load template
    template = loader.get_template("faq.html")

    return render(request, 'faq.html', {})