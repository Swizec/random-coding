from django.db import models

# Create your models here.

class A(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return "A: %d" % self.id

class B(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    A = models.ForeignKey(A)
    num = models.IntegerField()
