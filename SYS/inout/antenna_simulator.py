from django.forms import ModelForm
from inout.models import Entry
from django.http import HttpResponse

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['entry_type', 'rfid', 'structure']

def add_entry(request):
    '''
    Perform the insert statement of the POSTed form
    '''
    
    from inout.models import Entry, Structure
    from main.models import RFIDtag
    from datetime import datetime
    
    
    if request.method == 'POST': 

        # getting values from POSTed form      
        rx = request.POST.get('rfid') # returns the pk of the posted rfid
        sx = request.POST.get('structure') # returns the pk of the posted structure
        ex = request.POST.get('entry_type') # returns the pk of the posted entry_type
        dx = datetime.now() # actual datetime
        
        r=RFIDtag.objects.get(pk=rx) # get the instance of the posted rfid because it is a foreign key
        s=Structure.objects.get(pk=sx) # get the instance of the posted structure because it is a foreign key

        # performing the insert statement
        e = Entry(
            entry_type=ex,
            rfid=r,
            action_date=dx,
            structure=s
            )
        e.save()
        #e = [r,s]
    else:
        return HttpResponse("Error")
    
    return HttpResponse(e)
