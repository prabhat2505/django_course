from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':'this is set'
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("This is about")

def services(request):
    return HttpResponse("This is services")

def contact(request):
    return render(request,'contact.html')
