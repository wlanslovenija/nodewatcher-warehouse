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

class ItemType(models.Model):
    name = models.CharField(max_length=50, help_text='Name of the item type (e.g. router Linksys WRT54GL, RJ45 crimping tools)')
    note = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category)
    date_added = models.DateField(blank=True)
    atts = models.ManyToManyField(Attribute, blank=True, null=True)
    
    def __str__(self):
        return u"%s %s" % (str(self.id), self.name)
    
    def nice_repr(self):
        if self.note != "":
            return "%s (%s)" % (self.name, self.note)
        else:
            return str(self.name)

class Item(models.Model):
    # property status
    STATUS_CHOICES = (
            #('sold', 'Sold'),
            #('sold_hold', 'Sold but not payed'),
            #('ordered', 'Ordered'),
            #('shop', 'Available for sale'),
            ('borrowed', 'Borrowed'),
            ('broken', 'Broken'),
            ('wlan-si', 'Used for wlan-si infrastructure'),
            ('warehouse', 'In the warehouse'),
            ('private', 'Private')
    )
    
    name = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    item_type = models.ForeignKey(ItemType)
    
    status = models.CharField(max_length=50, choices = STATUS_CHOICES)
    mac = models.CharField(max_length = 17, blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    last_change = models.DateField(blank=True, null=True)
    
    amount = models.IntegerField(blank=True, null=True)
    
    # location
    location = models.ForeignKey(Location, blank=True, null=True)
    # ref to people in DB
    member = models.ForeignKey(User, blank=True, null=True)
    # ref to hot spot location
    node = models.ForeignKey(Node, blank=True, null=True)
    # ref to person not in DB
    person = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def nice_location(self):
        if self.node:
            return "Node: %s" % self.node.config.core.general().name
        elif self.member:
            return "%s %s (%s)" % (self.member.first_name, self.member.last_name, self.member.username)
        elif self.location:
            return self.location.name
        elif self.person != "" or self.email != "":
            return ", ".join(filter(lambda x: x != "" and x, [self.person, self.phone, self.email]))
        return ""
    
    def __str__(self):
        return "%s %s" % (self.name, str(self.mac))