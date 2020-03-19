from django.urls import path
from cars.views import CarsList

urlpatterns = [
    path('', CarsList.as_view(), name='cars_list_url'),

]