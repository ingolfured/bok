from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,primary_key=True)
    phone = models.DecimalField(max_digits=7,decimal_places=0,unique=True)
    address = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    ipaddress = models.IPAddressField()
    
    def __unicode__(self):
        return self.email

class Book(models.Model):
    created_by = models.ForeignKey('User')
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_year = models.DecimalField(max_digits=4,decimal_places=0)
    pub_nr = models.DecimalField(max_digits=3,decimal_places=0)
    ISBN = models.DecimalField(max_digits=13,decimal_places=0,primary_key=True)
    pic_url = models.URLField()
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name + "  ISBN:" + self.ISBN

class Ad(models.Model):
    user = models.ForeignKey('User')
    book = models.ForeignKey('Book')
    timestamp = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    state = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.user + "  " + self.book + "  Price:" + self.price
