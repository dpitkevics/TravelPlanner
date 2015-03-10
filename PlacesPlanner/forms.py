from django import forms

from TravelPlanner.lib.forms import Form


class PlaceSearchForm(Form):
    destination_city = forms.CharField(label='Destination City', max_length=100)

