from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return  HttpResponse('This is my first page')
    a = 5 + 6
    # return render(request,'about.html', {'gretting':'hello'})
    return render(request, 'about.html', {'gretting': a})

def home(request):
    return HttpResponse('This is my home')