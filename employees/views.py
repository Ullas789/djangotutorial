from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def employee(request):
    return HttpResponse("Hello, world. You're at the employee index.")