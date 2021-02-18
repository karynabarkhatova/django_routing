from django.shortcuts import render
from django.http import HttpResponse


def post_view(request):
    html = '<html><body><h1>Hello! You are in app "POST"</h1></body></html>'
    return HttpResponse(html)

