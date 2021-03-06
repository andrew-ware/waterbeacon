from django.contrib import admin
from app import models
from utils.log import log
from copy import deepcopy
# Register your models here.

def register_admin(model):
    """Turn admin.site.register into a decorator."""
    def wrapper(klass):
        admin.site.register(model, klass)
        return klass
    return wrapper

@admin.register(models.sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name','type','units','mean','std')
    list_filter = ('type',)
    search_fields = ['name']

#def reset_nodesim(modeladmin, request, queryset):
#    for qs in queryset:
#    	pass

#def stop_nodesim(modeladmin, request, queryset):
#    for qs in queryset:
#    	pass

#def start_nodesim(modeladmin, request, queryset):
#    for qs in queryset:
#    	pass

def copy_simnode(modeladmin, request, queryset):
    for qs in queryset:
        simnode = deepcopy(qs)
        simnode.name = "%s (copy)" % qs.name
        simnode.pk = None
        simnode.save()
        simnode.sensors.add(*qs.sensors.all())

@admin.register(models.sim_node)
class SimNodeAdmin(admin.ModelAdmin):
    list_display = ('name','devicealias','measurement_count')

    search_fields = ['devicealias']
    search_fields = ['name']
    filter_horizontal = ('sensors',)

    actions = [copy_simnode]

class TagInline(admin.TabularInline):
    model = models.tag

@admin.register(models.node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name','active','long','lat','sourcetype','devicealias','notes')
    list_filter = ('active','sourcetype')
    search_fields = ['name']
    inlines = [
        TagInline,
    ]
    readonly_fields = ('ph_chart', 'temperature_chart','conductivity_chart','turbidity_chart','orp_chart','odo_chart')
    fieldsets = [
            ('Node', { 'fields':  [  'active', 'name', 'long', \
                            'lat', 'devicealias', 'sourcetype','commtype','deviceaddress','hostip','proxy_url','notes' ]}), \
            ('Ph', { 'fields':  [  'ph_chart',  ]}),
            ('Temperature', { 'fields':  [  'temperature_chart',  ]}),

            ('Conductivity', { 'fields':  [  'conductivity_chart',  ]}),
            ('Turbidity', { 'fields':  [  'turbidity_chart',  ]}),
            ('Oxygen Reduction Potential', { 'fields':  [  'orp_chart',  ]}),
            ('Dissolved Oxygen', { 'fields':  [  'odo_chart',  ]}),
    ]

    class Media:
        js = ("js/node.js",)
