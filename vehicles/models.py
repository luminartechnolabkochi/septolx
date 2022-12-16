from django.db import models

# Create your models here.


class Vehicles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    color=models.CharField(max_length=100,null=True)
    options=(
        ("diesel","diesel"),
        ("petrol","petrol"),
        ("cng","cng"),
        ("ev","ev")
    )

    fuel_type=models.CharField(max_length=200,choices=options,default="petrol")
    pyear=models.DateField(null=True)
    runningkm=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    user=models.CharField(max_length=200)

    def __str__(self) :
        return self.name