from django.contrib import admin
from vehicle.models import Booking, Brands
from vehicle.models import Vehicles

# Register your models here.
# class BrandsAdmin(admin.ModelAdmin):
    # list_display = ('name', 'description', 'logo')

# class VehiclesAdmin(admin.ModelAdmin):
    # list_display = ('brand_id', 'name', 'model', 'status', 'rent_per_hour', 'description', 'image')

admin.site.register((Brands, Vehicles, Booking))
# admin.site.register(Vehicles)