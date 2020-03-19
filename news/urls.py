from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'news'
urlpatterns = [
    path('news/', NewsList.as_view(), name='list_view_url'),
]