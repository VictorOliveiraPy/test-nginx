from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(BaseModel):
    name = models.CharField(max_length=200)
    descripiton = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    gtin = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

