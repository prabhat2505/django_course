from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is index")

def about(request):
    return HttpResponse("This is about")
