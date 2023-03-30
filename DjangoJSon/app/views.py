from django.shortcuts import render

import requests
import json

def my_view(request):
    url = "https://raw.githubusercontent.com/bambadiagne/github-user-stats/master/users.json"
    response = requests.get(url)
    data = json.loads(response.text)# Ajouter cette ligne
    return render(request, 'template.html', {'data': data})
