from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import xml
from wishlist.views import show_json
from wishlist.views import json_id 

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', xml, name='xml'),
    path('json/', show_json, name='json'),
    path('json/<int:id>', json_id, name='json_id'), #sesuaikan dengan nama fungsi yang dibuat
]