from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES=(
    ('EX','Exercise'),
    ('DT','Dieat'),
    ('HT','Health'),
    ('YG','Yoga'),
    ('MD','Meditation'),

)





class Product(models.Model):
    title = models.CharField(max_length=100)
    time = models.FloatField()
    sets = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    




DIET_TYPE=(
    ('MG','Muscle Gain'),
    ('Wl','Weight Loss'),
    ('ND','Normal Diet'),
)


class Diet(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(choices=DIET_TYPE, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    # state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    

class Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product
