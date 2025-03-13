from django.http import HttpResponse

def landing_page(req):
    return HttpResponse("Hello world of polls!")