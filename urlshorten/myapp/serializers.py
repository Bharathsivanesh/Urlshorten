from rest_framework import serializers
from .models import Urlshorten

class UrlShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urlshorten
        fields = ['id', 'Long_url', 'Short_url', 'Created_at']
