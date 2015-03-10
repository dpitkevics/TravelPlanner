import foursquare

from TravelPlanner import settings


def get_client():
    client = foursquare.Foursquare(settings.FOURSQUARE_CLIENT_ID, settings.FOURSQUARE_CLIENT_SECRET)

    return client