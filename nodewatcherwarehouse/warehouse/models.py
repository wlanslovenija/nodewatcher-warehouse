from django.db import models
from macaddress import fields

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    gps_x = models.IntegerField(blank=True)
    gps_y = models.IntegerField(blank=True)

    def __str__(self):
        return "%s (%s, %s)" % (self.name, str(self.gps_x), str(self.gps_y))

class Attribute(models.Model):
    name = models.CharField(max_length=50)
    att_type = models.CharField(max_length=50, blank=True)
    value = models.CharField(max_length=500)
    
    def __str__(self):
        return "%s=%s" % (self.name, str(self.value))

class Item(models.Model):
    # property status
    STATUS_CHOICES = (
            ('sold', 'Sold'),
            ('sold_hold', 'Sold but not payed'),
            ('ordered', 'Ordered'),
            ('shop', 'Available for sale'),
            ('borrowed', 'Borrowed'),
            ('broken', 'Broken'),
            ('wlan-si', 'Used for wlan-si infrastructure'),
            ('warehouse', 'In the warehouse')
    )
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, choices = STATUS_CHOICES)
    amount = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location, blank=True)
    date_added = models.DateField(blank=True)
    status_change = models.DateField(blank=True)
    last_change = models.DateField(blank=True)
    atts = models.ManyToManyField(Attribute)
    # ref to people
    # ref to hot spot location

class Instance(models.Model):
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, choices = Item.STATUS_CHOICES)
    mac = fields.MACAddressField(blank=True)
    date_added = models.DateField(blank=True)
    status_change = models.DateField(blank=True)
    last_change = models.DateField(blank=True)
    location = models.ForeignKey(Location)
    # ref to people
    # ref to hot spot location