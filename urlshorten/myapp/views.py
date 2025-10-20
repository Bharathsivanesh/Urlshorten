from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Urlshorten
from .serializers import UrlShortenSerializer
import requests

class UrlCreateView(APIView):
    def post(self, request):
        long_url = request.data.get("long")
        if not long_url:
            return Response({"message": "Field 'long' is required"}, status=status.HTTP_400_BAD_REQUEST)

        tinyurl_api = "https://tinyurl.com/api-create.php"
        response = requests.get(tinyurl_api, params={"url": long_url})
        if response.status_code != 200:
            return Response({"message": "Error creating short URL"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        short_url = response.text
        db = Urlshorten.objects.create(Short_url=short_url, Long_url=long_url)
        serializer = UrlShortenSerializer(db)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UrlListView(APIView):
    def get(self, request):
        urls = Urlshorten.objects.all()
        if not urls.exists():
            return Response({"message": "No URLs found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UrlShortenSerializer(urls, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class UrlDeleteView(APIView):
    def delete(self, request, id):
        try:
            url = Urlshorten.objects.get(id=id)
            url.delete()
            return Response({"message": "URL Deleted"}, status=status.HTTP_200_OK)
        except Urlshorten.DoesNotExist:
            return Response({"message": "URL not found"}, status=status.HTTP_404_NOT_FOUND)
