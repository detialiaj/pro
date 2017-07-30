from django.forms import ModelForm
from inout.models import Entry
from django.http import HttpResponse

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['entry_type', 'rfid', 'structure']

def add_entry(request):
    from inout.models import Entry, Structure
    from main.models import RFIDtag
    from datetime import datetime
    #message = 'its ok!'

    r=RFIDtag.objects.all() #should filter the exact tag by value and return it pk
    s=Structure.objects.all() #should filter the exact Structure by code and return it pk
    e = Entry(
        entry_type='In',
        rfid=r.get(pk='2'),
        action_date=datetime.now(),
        structure=s.get(pk=2)
        )
    e.save()
    return HttpResponse(e)
