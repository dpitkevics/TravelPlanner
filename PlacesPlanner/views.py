from django.shortcuts import render

import foursquare


def index(request):
    client = foursquare.Foursquare()

    context = {}

    return render(request, 'PlacesPlanner/index.html', context)