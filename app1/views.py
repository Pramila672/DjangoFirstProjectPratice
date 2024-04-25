from django.http import HttpResponse , HttpResponseNotFound
from django.views.decorators.http import require_http_methods , require_safe
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(3600)
#@require_safe()
#@require_http_methods(["POST"])
#@require_POST

def home(request):
    print("Hey caching is working fine")
    #print("Home is called.")
    return HttpResponse("<h1>This is my first view page</h1>" , status=500)
    #return HttpResponseNotFound("<h1>The Http request hasnot been found</h1>"