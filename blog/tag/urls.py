from django.urls import path
from tag.views import tag

urlpatterns = [
    path('', tag),
]
