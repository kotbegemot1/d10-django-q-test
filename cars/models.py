from django.db import models

# Create your models here.

class Car(models.Model): 
    TRANSMISSION = [
        [1, "механическая коробка передач"],
        [2, "автоматическая коробка передач"],
        [3, "роботизированная коробка передач"],
    ]
    manufacturer = models.CharField('Производитель', max_length=50, null=True)
    model = models.CharField("Модель", max_length=50, null=True)
    year_of_issue = models.IntegerField("Год выпуска",null=True)
    transmission = models.SmallIntegerField("Коробка передач",choices=TRANSMISSION, null=True)
    colour = models.CharField("Цвет",max_length=20, null=True)
    
    def __str__(self):
        return f'{self.manufacturer} - {self.model}'
    