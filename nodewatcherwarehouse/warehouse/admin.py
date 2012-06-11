from django.contrib import admin
from models import Category, Item, Location, Instance, Attribute

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )

class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "note", "status", "amount", "category", "location", )

class LocationAdmin(admin.ModelAdmin):
    pass

class InstanceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "note", "status", "mac", "location", "date_added", "status_change")

class AttributeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Instance, InstanceAdmin)
admin.site.register(Attribute, AttributeAdmin)
