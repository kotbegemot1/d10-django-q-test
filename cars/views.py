from django.shortcuts import render
from django.db.models import Q
from django.views.generic import View

from .models import Car
from .forms import CarForm

class CarsList(View):
    def get(self, request):
        if request.GET:
            form = CarForm(request.GET)
            cars = Car.objects.filter(
                Q(manufacturer__icontains=request.GET.get('manufacturer')) &
                Q(model__icontains=request.GET.get('model')) &
                Q(year_of_issue__gte=request.GET.get('year_of_issue')) &
                Q(transmission__icontains=request.GET.get('transmission')) &
                Q(colour__icontains=request.GET.get('colour')))
        else:
            form = CarForm()
            cars = Car.objects.all()
        return render(request, 'cars/cars_list.html', {'form': form, 'cars': cars})
