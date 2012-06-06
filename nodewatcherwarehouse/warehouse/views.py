from django.http import HttpResponse

def list(request):
    return HttpResponse("Hello world!")

def view(request, id):
    return HttpResponse("Hello %s!" % id)