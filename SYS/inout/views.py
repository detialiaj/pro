from django.shortcuts import render
from django.http import HttpResponse, Http404


def antenna_simulator(request):
    
    html_content = """<!DOCTYPE html>
<html>
<body>

<h1>antenna is turning on...</h1>
<ul>
Go to
<li><a href="/">Home</a> page.</li>
<li><a href="/manage/">Admin</a> page.</li>
<li><a href="/main/">Main app</a> page.</li>
</body>
</html>

"""
    return HttpResponse(html_content)
