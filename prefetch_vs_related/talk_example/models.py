from django.contrib import admin
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Pic(models.Model):
    title = models.CharField(max_length=30)
    href = models.CharField(max_length=300)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=30)
    pics = models.ManyToManyField(Pic)

class User(models.Model):
    name = models.CharField(max_length=10)

    pics = models.ManyToManyField(Pic)
    albums = models.ManyToManyField(Album)

class Comment(models.Model):
    pic = models.ForeignKey(Pic)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=100)


class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __unicode__(self):
        return u"%s (%s)" % (self.name, u", ".join([topping.name
                                                    for topping in self.toppings.all()]))
