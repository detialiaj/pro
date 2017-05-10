from django.contrib import admin
from inout.models import Structure, Entry


class StructureAdmin(admin.ModelAdmin):
    list_display = (
	'code',
	'name',
	'description',
	)
	
class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = (
    'id',
    'entry_type',
    'action_date',
    'rfid',
    'structure',	
)
    ordering = ['id', 'action_date']
    

admin.site.register(Structure, StructureAdmin)
admin.site.register(Entry, EntryAdmin)
# Register your models here.
