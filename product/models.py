from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    gtin = models.CharField(max_length=30)
    category = models.ManyToManyField('Category',verbose_name="list of categories")

    def __str__(self) -> str:
        return f"{self.name} - {self.description} - {self.price} - {self.stock} - {self.gtin} - {self.created_at} - {self.updated_at}"


    def get_all_categories(self):
        category = ''
        for cat in self.category.all():
            category += f' {cat},'
        return category.strip()


class Category(BaseModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"Nome: {self.name} - Descrição: {self.description}"
