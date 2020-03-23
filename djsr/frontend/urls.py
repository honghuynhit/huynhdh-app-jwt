from django.urls import path, re_path
from .views import index_view

urlpatterns = [
    path('', index_view), # the empty url
    re_path(r'^.*/$', index_view) # all other urls
]