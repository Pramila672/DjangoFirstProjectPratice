from django.http import HttpResponse , HttpResponseNotFound
from django.views.decorators.http import require_http_methods , require_POST

# Create your views here.
#@require_http_methods(["POST"])
@require_GET
#@require_POST
def home(request):
    print("Home is called.")
    return HttpResponse("<h1>This is my first view page</h1>" , status=500)
    #return HttpResponseNotFound("<h1>The Http request hasnot been found</h1>"