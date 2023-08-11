# v1. from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger



def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    
    context = {
        "bibi": burgers,
    }
    return render(request, "burger_list.html", context)


''' v1
def main(request):
    context = '<h1>Hello</h1>'
    return HttpResponse(context)

def burger_list(request):
    context = "Burger List"
    return HttpResponse(context)
'''

