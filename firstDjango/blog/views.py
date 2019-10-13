from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(Request):
    return HttpResponse('<h1>Blog home</h1>')

def about(Request):
    return HttpResponse('<h1>Blog about</h1>')
