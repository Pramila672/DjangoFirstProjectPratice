from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    print("Home is called.")
    return HttpResponse("<h1>This is my first view page</h1>")