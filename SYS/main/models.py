from django.db import models
import datetime

#This will be the base for other models
class CommonModel(models.Model):
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Item(CommonModel):
    #code = models.CharField(max_length=25, unique=True)
    #name = models.CharField(max_length=250)
    description = models.TextField(max_length = 1000)
    unit = models.ForeignKey('Unit')
    date_created = models.DateTimeField(auto_now_add=True)  
    last_modified = models.DateTimeField(auto_now=True) #or 'default=datetime.datetime.now()'
    qrcode = models.CharField(max_length=255, null=True, blank=True, verbose_name='QR Code')
    active = models.BooleanField(default = True)
    
    def __str__(self):
       return self.code
       #return 'Desc: {}'.format(self.description)
	   
    class Meta:
	    verbose_name= "Item"
	    verbose_name_plural = "Items"

    # Conversion for 'date_created' field to be displayed as short-date format
    def short_date_convert(self):
        #return self.DateTimeField.strftime("%d %m %Y")
        return format(self.date_created, "%d-%m-%Y %H:%M")
    
    # Apply line below to make possible to order the edited column
    short_date_convert.admin_order_field= ('date_created') # Should remove this peace of code from model file
    short_date_convert.short_description = 'Date Created'
            
    
class Unit(CommonModel):
    #code = models.CharField(max_length=25, unique = True)
    #name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
	    verbose_name= "Unit"
	    verbose_name_plural = "Units"
	
class Barcode(models.Model):
    barcode = models.CharField(max_length=50, unique=True)
    item = models.ForeignKey('Item')
    
    def __str__(self):
        return self.barcode
    
    class Meta:
        verbose_name = "Barcode"
        verbose_name_plural = "Barcodes"		

class RFIDtag(models.Model):
    value = models.CharField(max_length=250, unique=True, null=True)
    item = models.ForeignKey('Item')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'RFID tag'
        verbose_name_plural = 'RFID tags'


