from django.shortcuts import render
from django.http import HttpResponse, Http404
from main.models import *
from django.apps import apps
import os

# The common content
common_content = {
    'applist':('Main', 'Inout')} 
myapp = apps.get_app_config('main')
model_list = myapp.models

def get_model_by_label(model_label, app_name):
    app=apps.get_app_config(app_name)
    model=app.get_model(model_label)
    return model

def dashboard(request):
    content = common_content.copy()
    content['title'] = "Dashboard"
    return render(request, 'main/base.html', content)

def main_page_models(request):
    
    content = common_content.copy()
    content['title'] = myapp.verbose_name
    content['item_list'] = model_list
    #content={'title':myapp.verbose_name, 'item_list':model_list}
    return render(request, 'main/base.html', content)

	
# The working area views listed below
# don't forget to use raise in case of errors
def main_page_models_detailed(request, model):
    
    try:
        active_model=get_model_by_label(model, 'main')
    except LookupError:
        raise Http404("No model named '%s'." %model)
    model_detailed = active_model.objects.all()
    content = common_content.copy()
    content['title'] = active_model._meta.verbose_name_plural
    content['item_list'] = model_detailed
    return render(request, 'main/base.html', content)


def no_page_yet(request):
    html_content = """<!DOCTYPE html>
<html>
<body>

<h1>No page yet...</h1>
<ul>
Go to
<li><a href="/">Home</a> page.</li>
<li><a href="/manage/">Admin</a> page.</li>
<li><a href="/main/">Main app</a> page.</li>
</body>
</html>"""
    
    return HttpResponse(html_content)

