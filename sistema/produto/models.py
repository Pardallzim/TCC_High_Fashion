from django.db import models
from users.models import User
from tipo.models import Type
from colecao.models import Collection
from parametros.models import Parameters

# Create your models here.

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    path = models.ImageField(upload_to='img/%Y/%m/%d/')

    def __str__(self):
        return self.name
    
    def user_commented(self, user):
        return CommentPage.objects.filter(id_user=user).exists()
    
    def product_commented(self, user):
        return CommentProduct.objects.filter(id_product=self, id_user=user).exists()

class ProductCost(models.Model):
    parameters = models.ForeignKey(Parameters, on_delete=models.CASCADE)
    raw_materials = models.DecimalField(max_digits=8, decimal_places=2)
    labor = models.DecimalField(max_digits=8, decimal_places=2)
    indirect = models.DecimalField(max_digits=8, decimal_places=2)

    def get_price_cost(self):
        return (self.materials + self.work + self.indirect)

    def get_price_sell(self):
        return self.get_price_cost / self.parameters.get_divisor

class CommentProduct(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'{self.id_user} on {self.id_product}'

class CommentPage(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment