import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SYS.settings')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import django
django.setup()

# from main.models import *
"""
unit_list = ['unit%s' %i for i in range(6,10)]

# print("add_unit(code="", name="")")
def add_unit():
    for i in unit_list:
        i = Unit.objects.create(code=i, name=i)
        i.save()
    return i

add_unit()
"""


    
