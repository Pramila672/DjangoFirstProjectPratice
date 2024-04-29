from django.http import HttpResponse , HttpResponseNotFound
from django.views.decorators.http import require_http_methods , require_safe
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
# Create your views here.
#@cache_page(3600)
#@require_safe()
#@require_http_methods(["GET"])
@login_required

def home(request):
    #print("Hey caching is working fine")
    #print("Home is called.")
    #return HttpResponse("<h1>This is my first view page</h1>")
    #return HttpResponseNotFound("<h1>The Http request hasnot been found</h1>"
    #return render(request , "app1/home.html")
    return redirect (login)

def login(request):
    return HttpResponse("<h1> This is my login page </h1>")
   # return render(request, "login.html")
