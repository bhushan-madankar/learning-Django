from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world! This is the home page of the chaiDjango project.")
    return render(request, 'index.html')

def About(request):
    return HttpResponse("Hello, world! This is the about page of the chaiDjango project.")

def Contact(request):
    return HttpResponse("Hello, world! This is the contact page of the chaiDjango project.")
