from django.urls import path
from .views import main, getForecastData, getLocationData

urlpatterns = [
    path('', main),
    path('location/', getLocationData),
    path('forecast/', getForecastData),
]
