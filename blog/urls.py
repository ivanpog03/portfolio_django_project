from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import include

urlpatterns = [
    path('', views.all_blogs, name='all blogs'),
]