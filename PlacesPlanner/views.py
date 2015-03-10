from django.shortcuts import render

from PlacesPlanner.forms import PlaceSearchForm
from TravelPlanner.lib import foursquare

from TravelPlanner.lib.vk import vk_api


def index(request):
    vk_api('database.getCountries', {'need_all': 0, 'count': 100})

    if request.method == 'POST':
        form = PlaceSearchForm(request.POST)

        destination_city = request.POST['destination_city']

        client = foursquare.get_client()
        explore_venues = client.venues.explore({'near': destination_city, 'section': 'sights'})
    else:
        form = PlaceSearchForm()
        explore_venues = None

    context = {
        'form': form,
        'explore_venues': explore_venues,
    }

    return render(request, 'PlacesPlanner/index.html', context)


def category_list(request):
    client = foursquare.get_client()

    categories = client.venues.categories()

    context = {
        'categories': categories['categories']
    }

    return render(request, 'PlacesPlanner/category_list.html', context)