from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def home(request : HttpRequest):
    # return HttpResponse("Hello world!")
    return render(request, "home/home.html")
