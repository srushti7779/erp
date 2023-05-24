from django.db import models

# Create your models here.


PRODUCT_CHOICES = (
    ('console-table','console-table'),
    ('bench', 'bench'),
    ('dinning-table','dinning-table'),
    ('side-table','side-table'),
    ('coffee-table','coffee-table'),
    ('pedestal-light','pedestal-light'),
)

class Products(models.Model):
    name = models.CharField(max_length=200)
    typeOfProduct = models.CharField(max_length=14, choices=PRODUCT_CHOICES, default='bench')
    description = models.TextField()
    imagebw1 = models.ImageField(upload_to='productImage' ,default="1.jpg")
    imageclr2 = models.ImageField(upload_to='productImage',default="1.jpg")
    image3 = models.ImageField(upload_to='productImage',default="1.jpg")
    image4 = models.ImageField(upload_to='productImage',default="1.jpg")

    def str(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('interiors','interiors'),
    ('furniture', 'furniture'),
    ('installation','installation'),
)


class Project(models.Model):

    category = models.CharField(max_length=14, choices=CATEGORY_CHOICES, default='interiors')
    image1 = models.ImageField(upload_to='projectsImage')
    image2 = models.ImageField(upload_to='projectsImage')
    
    def str(self):
        return str(self.id)