from django.urls import path
from . import views
urlpatterns=[
    path('post/',views.store_url),
path('get/',views.get_url)
]