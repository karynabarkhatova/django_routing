from django.contrib import admin
from django.urls import path, include

from editor.views import editor
from tag.views import tag
from post.views import post

urlpatterns = [
    path('admin/', admin.site.urls),
    path("app/post/", post),
    path('app/tag/', tag),
    path('app/editor/', editor),
    path('post/', include('post.urls')),
    path('tag/', include('tag.urls')),
    path('editor/', include('editor.urls')),
]
    
