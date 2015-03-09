import requests
import json

from django.shortcuts import render


def index(request):
    response = requests.get('http://www.flysiesta.lv/xhr2/search/id/RIX/MLE/2015-07-20/2015-07-26/adt-2/chd-0/inf-0/')
    data = json.loads(response.text)

    print(data)

    context = {}

    return render(request, 'FlightPlanner/index.html', context)