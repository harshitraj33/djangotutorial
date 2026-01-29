from django.shortcuts import render

from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the index page.")

def index(request):
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("This is the contact page.")

def about(request):
    return HttpResponse("This is the about page.")
