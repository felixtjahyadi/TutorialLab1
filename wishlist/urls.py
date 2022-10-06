from unicodedata import name
from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import xml
from wishlist.views import show_json
from wishlist.views import json_id 
from wishlist.views import register 
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import show_wishlist_ajax
from wishlist.views import wishlist_form

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', xml, name='xml'),
    path('json/', show_json, name='json'),
    path('json/<int:id>', json_id, name='json_id'), 
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_wishlist_ajax, name="ajax"),
    path('ajax/submit', wishlist_form, name="form")
]