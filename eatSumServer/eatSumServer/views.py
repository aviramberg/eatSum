from django.http import HttpResponse

__author__ = 'lenovo'

def index(request):
    return HttpResponse("hi bye")