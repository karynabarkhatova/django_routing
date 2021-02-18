from django.contrib import admin
from django.urls import path
from editor.views import editor_view
from tag.views import tag_view
from post.views import post_view

urlpatterns = [
    path('app/post/', post_view),
    path('app/tag/', tag_view),
    path('app/editor/', editor_view),
    path('post/', post_view),
    path('tag/', tag_view),
    path('editor/', editor_view),
]
    
