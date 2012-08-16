from django.db import models
from macaddress import fields

from nodewatcher.nodes.models import Node
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Attribute(models.Model):
    name = models.CharField(max_length=50)
    att_type = models.CharField(max_length=50, blank=True)
    value = models.CharField(max_length=500)
    
    def __str__(self):
        return "%s=%s" % (self.name, str(self.value))

class Item(models.Model):
    name = models.CharField(max_length=50, help_text='Name of the item (e.g. router Linksys WRT54GL, RJ45 crimping tools)')
    note = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category)
    date_added = models.DateField(blank=True)
    atts = models.ManyToManyField(Attribute, blank=True, null=True)
    
    def __str__(self):
        return u"%s %s" % (str(self.id), self.name)

class Instance(models.Model):
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
    item = models.ForeignKey(Item)
    
    status = models.CharField(max_length=50, choices = STATUS_CHOICES)
    mac = fields.MACAddressField(blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    last_change = models.DateField(blank=True, null=True)
    
    amount = models.IntegerField(blank=True, null=True)
    
    # location
    location = models.ForeignKey(Location, blank=True, null=True)
    # ref to people
    member = models.ForeignKey(User, blank=True, null=True)
    # ref to hot spot location
    node = models.ForeignKey(Node, blank=True, null=True)
    
    def __str__(self):
        return "%s %s" % (self.name, str(self.mac))