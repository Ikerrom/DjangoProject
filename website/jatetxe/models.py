from django.db import models

class Sukaldari(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    photo = models.TextField()

class Platera(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.FloatField()
    photo = models.TextField()
    sukaldari = models.ForeignKey(Sukaldari,on_delete = models.CASCADE, null = True)

class Total(models.Model):
    totalprice = models.FloatField()
