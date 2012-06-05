from django.contrib import admin
from models import Category, Item, Location, Instance, Attribute

class CategoryAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class InstanceAdmin(admin.ModelAdmin):
    pass

class AttributeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Instance, InstanceAdmin)
admin.site.register(Attribute, AttributeAdmin)