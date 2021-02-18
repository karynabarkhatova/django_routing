from django.shortcuts import render
from django.http import HttpResponse


def editor_view(request):
    html = '<html><body><h1>Hello! You are in app "EDITOR"</h1></body></html>'
    return HttpResponse(html)
