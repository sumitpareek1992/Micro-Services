from django.shortcuts import redirect, render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Warehouse Page")