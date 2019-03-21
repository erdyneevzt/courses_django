from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Home Page!")

def items(request):
    return HttpResponse("Welcome to localhost/items")

def day_archive(request, year , month, day):
    return HttpResponse("Welcome to localhost/items/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})$")

def render_template(request):
    return render(request, "main.html", {}) #

def form_handler(request):
    if request.POST:
        return HttpResponse("Request is POST")
    else:
        return HttpResponse("Request is GET")