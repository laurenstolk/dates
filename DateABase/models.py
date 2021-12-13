from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator  
# Create your models here.

class Season(models.Model):
    season = models.CharField(max_length=35)

    def __str__(self) :
        return (self.season)

# class Location(models.Model) :
#     locationName = models.CharField(max_length=30)
#     ambiance = models.CharField(max_length=20)
    
#     def __str__(self) :
#         return (self.locationName)

class DateType(models.Model) :
    typeName = models.CharField(max_length=20)

    def __str__(self) :
        return (self.typeName)

class Price(models.Model):
    price_category= models.CharField(max_length=15, unique=True)

    def __str__(self) :
        return (self.price_category)

class Date(models.Model) :
    dateName = models.CharField(max_length=50, verbose_name="Name of Date")
    dateTypeID = models.ForeignKey('DateType', null=False, blank=False, verbose_name="Date Type", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    locationName = models.CharField(max_length=30, verbose_name="locationName")
    # locationID = models.ForeignKey('Location', null=False, blank=False, on_delete=models.DO_NOTHING)
    priceRating = models.ForeignKey('Price', null=False, blank=False, verbose_name="Price", on_delete=models.DO_NOTHING, to_field='id')
    date_season = models.ManyToManyField('Season', verbose_name="Best Season for Date")  
    
    def __str__(self) :
        return (self.dateName)