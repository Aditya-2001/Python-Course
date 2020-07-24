from django.shortcuts import render,HttpResponse

# Create your views here.
def homescreen(request):
    return HttpResponse("<h1>Welcome to Home screen of First App</h2>")