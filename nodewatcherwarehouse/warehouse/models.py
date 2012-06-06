from django.db import models
from macaddress import fields

class Category(models.Model):
    name = models.CharField(max_length=50)

class Location(models.Model):
    name = models.CharField(max_length=50)
    gps_x = models.IntegerField()
    gps_y = models.IntegerField()

class Attribute(models.Model):
    name = models.CharField(max_length=50)
    att_type = models.CharField(max_length=50)
    value = models.CharField(max_length=500)

class Item(models.Model):
    STATUS_CHOICES = (
            ('Sold', 'Sold'),
            ('Borrowed', 'Borrowed'),
            ('Broken', 'Broken'),
            ('Shop', 'Shop'),
            ('Wlan-si', 'Used at wlan-si.net'),
            ('', '')
    )
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices = STATUS_CHOICES)
    amount = models.IntegerField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    date_added = models.DateField()
    status_change = models.DateField()
    last_change = models.DateField()
    atts = models.ManyToManyField(Attribute)
    # ref to people
    # ref to hot spot location

class Instance(models.Model):
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices = Item.STATUS_CHOICES)
    mac = fields.MACAddressField()
    date_added = models.DateField()
    status_change = models.DateField()
    last_change = models.DateField()
    location = models.ForeignKey(Location)
    # ref to people
    # ref to hot spot location