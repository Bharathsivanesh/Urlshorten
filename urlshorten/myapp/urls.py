from django.urls import path
from .views import UrlCreateView, UrlListView, UrlDeleteView

urlpatterns = [
    path('urls/', UrlListView.as_view(), name='url-list'),
    path('urls/create/', UrlCreateView.as_view(), name='url-create'),
    path('urls/delete/<int:id>/', UrlDeleteView.as_view(), name='url-delete'),
]
