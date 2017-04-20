from django.db import models
from main import models as main_models

class Structure(models.Model):
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True)
	# type, component needs to be added
	# type for warehouse, office, building, field etc.
	
	
    def __str__(self):
        return self.code

		
class Entry(models.Model):
    
    OPTION_LIST = (
    ('In', 'In'),
    ('Out', 'Out'),
    )
    type = models.CharField(max_length=3, choices=OPTION_LIST)
    rfid = models.ForeignKey('main.RFIDtag')
    action_date = models.DateTimeField(auto_now_add=True)
    structure = models.ForeignKey('Structure')

    class Meta:
	    verbose_name_plural = "Entries"
	
    def __str__(self):
        return str(self.id)
