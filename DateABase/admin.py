from DateABase.models import Date
from django.contrib import admin
from .models import Date, DateType, Season, Price

# Register your models here.
admin.site.register(Date)
# admin.site.register(Location)
admin.site.register(DateType)
admin.site.register(Season)
admin.site.register(Price)