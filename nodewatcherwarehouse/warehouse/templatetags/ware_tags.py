from django import template
register = template.Library()
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

def qr_code(obj, size=2):
    return reverse("wh:qr", kwargs={"string": abs_view(obj), "size":size})

def abs_view(obj):
    from django.contrib.sites.models import Site
    # TODO Somehow check for https?
    return "%s://%s%s" % ("http", Site.objects.get_current().domain, reverse("wh:item-detail", kwargs = {"pk" : obj.id}))

def nice_location(obj):
    if obj.node:
        return "Node: %s" % obj.node.config.core.general().name
    elif obj.location:
        return obj.location.name
    return ""


def nice_ownership(obj):
    if obj.member:
        return "%s %s (%s)" % (obj.member.first_name, obj.member.last_name, obj.member.username)
    elif obj.person != "" or obj.email != "":
        if obj.email:
            return mark_safe("<a href='mailto:%s'>%s</a> %s" % (obj.email, obj.person, obj.phone or ""))
        else:
            return "%s %s" % (obj.person, obj.phone or "")
    return ""

register.filter("qr_code", qr_code)
register.filter("abs_view", abs_view)
register.filter("nice_ownership", nice_ownership)
register.filter("nice_location", nice_location)