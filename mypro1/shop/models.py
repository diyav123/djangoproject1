from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='shop/categories',blank=True,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    image = models.ImageField(upload_to='shop/categories', blank=True, null=True)
    stock=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name