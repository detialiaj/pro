from django.shortcuts import render
from django.http import HttpResponse, Http404
from .antenna_simulator import EntryForm


def antenna_simulator_form(request):
    form=EntryForm()
    
  
    return render(request, 'antenna_simulator.html', {'form':form, 'is_bound': form.is_bound})
