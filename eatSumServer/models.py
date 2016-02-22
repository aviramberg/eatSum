# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class Resturants(models.Model):
    name = models.CharField(max_length=100)
    foodType = models.CharField(max_length=100)

# many to one relationship pizza has a resturant
class Pizza(models.Model):
    Resturants = models.ForeignKey(Resturants, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

# many to one relationship burger has a resturant
class Burger(models.Model):
    Resturants = models.ForeignKey(Resturants, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

# many to one relationship sushi has a resturant
class Sushi(models.Model):
    Resturants = models.ForeignKey(Resturants, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

# many to one relationship MenuPizza has a Pizza
class MenuPizza(models.Model):
    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    price = models.IntegerField()

class MenuBurger(models.Model):
    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    price = models.IntegerField()

class MenuSushi(models.Model):
    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    price = models.IntegerField()

class OrderDB(models.Model):
    orderMaker = models.CharField(max_length=100)





    class Meta:
        managed = False
        db_table = 'test_table'
