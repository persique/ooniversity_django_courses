from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the quadratic index.")

def results(request, a, b, c):
   
    return render(request,  "results.html")



