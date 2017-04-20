from django.contrib import admin, messages
from django.contrib.auth.models import User, Group
from django.forms import TextInput, Textarea, ModelForm
from django.http import HttpResponseRedirect, QueryDict, HttpResponse
from django.shortcuts import render, get_object_or_404

from main.models import *


"""
Special cases aren't special enough to break the rules
"""

my_models =[
    #Item,
    #Barcode,
    Unit,
    RFIDtag,
      ]

# Adding an action that performs the "Save As" command
def save_as_action_admin(modeladmin, request, queryset):
    rows = len(queryset)
 
    """
    Selected objects == 0, is handled by django itself and return a warning message.
    Anyway such controls should be done on client-side. Basically there's not need to send a request
    in server because we already have the set of selected items.
    """
    if rows > 1:
        
        messages.warning(request, "This action can't be executed with %s objects selected. \
                                              You should select only one." % rows)
    else:
        """
        return HttpResponse(queryset)
        """
        selected_item = get_object_or_404(queryset)
        form = ItemForm(instance=selected_item) # ItemAdmin(selected_item, admin_site=queryset.model)
        return render(request, "admin/save_as_action.html", {'test_action': form,
                                                                                 'list': (1,2,3), #testting phase
                                                                                 'random_obj': '',
                                                                                 'opts': modeladmin.model._meta})
                
        
save_as_action_admin.short_description = "Save As New"

class BarcodeAdmin(admin.ModelAdmin):
    
    list_display = ('barcode','item',)

class BarcodeInline(admin.TabularInline):
    model = Barcode
    extra = 0

class ItemAdmin(admin.ModelAdmin):
       
    search_fields = ('code', 'name',)
    list_display = (
                    'code',
                    'unit',
                    'name',
                    'short_date_convert', # Attribute from ModelAdmin 
                    'active') # Elements displayed in the items list or so called change list
    
    list_filter = ('active',)
    readonly_fields = ('date_created','last_modified',)
    save_as = True # To use in case of a 'Clone' button
    fieldsets = (
        (None, {
            'fields': ('code', ('name', 'unit', 'active'), ('description', 'qrcode'),)# Fields to be desplyed in the add form, in this given order
            }),
        ('Show more', {
            'classes': ('collapse',),
            'fields': ('date_created','last_modified',),

            }),
        )
    inlines = [BarcodeInline]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs= {'size': '20'})},
        models.TextField: {'widget': Textarea (attrs= {'rows': 4, 'cols':40})},
        }
    actions = [save_as_action_admin]

    #list_display_links = (None) # Sets a hyperlink at each column in the list. If 'None', no modification allowed.
    #list_editable = ('description',) # This fields can be edited directly from the list


class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = ['code', 'name', 'description', 'unit', 'active']


class EntryForm(ModelForm):
    pass


# Set action controller at the bottom of the list in all models
admin.ModelAdmin.actions_on_top = False
admin.ModelAdmin.actions_on_bottom = True

# Register models and modeladmin's
admin.site.register(my_models)
admin.site.register(Item, ItemAdmin)
admin.site.register(Barcode, BarcodeAdmin)

# Adding actions to all change-lists
admin.site.add_action(save_as_action_admin)

# Removing Groups and users from admin site
# admin.site.unregister(Group) 
# admin.site.unregister(User)
