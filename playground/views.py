from django.shortcuts import render
# from django.http import HttpResponse

# def say_hello(request):
#     return HttpResponse('Hello World')

from django.http import HttpResponse

def calculate():
    x = 1
    y = 2
    return x

def index(request):
    # return HttpResponse("Hello World!")
    x = calculate()
    return render(request, 'hello.html', {'name': 'Ruchi'}) 