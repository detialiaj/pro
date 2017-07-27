from django.forms import ModelForm
from inout.models import Entry
from django.http import HttpResponse

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['entry_type', 'rfid', 'structure']

def add_entry(request):
    message = 'its ok!'
    return HttpResponse(message)
