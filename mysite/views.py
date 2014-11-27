from django.http import HttpResponse


def home(request):
    html = "<html><body><h1>Welcome to Video Sense API Home.<h1></body></html>"
    return HttpResponse(html)