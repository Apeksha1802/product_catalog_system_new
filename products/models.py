from django.db import models

# Create your models here.
# category model created
class CategoryModel(models.Model):
  category_name = models.CharField(max_length=50, unique=True)
  def __str__(self):
        return self.name

# product model created
class ProductModel(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    category_name=models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name