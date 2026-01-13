

from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarModel)
# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1  # Number of empty forms to show


# CarModelAdmin class
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Registering the inline


# CarMakeAdmin class with CarModelInline
admin.site.register(CarMake, CarMakeAdmin)
# Register models here
