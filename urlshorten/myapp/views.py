from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

from .models import Urlshorten

@csrf_exempt
def store_url(request):
    if request.method=="POST":
        try:
            load=json.loads(request.body)
            short=load.get('short')
            long=load.get('long')
            if not short or not long:
                return JsonResponse({"Messahe":"Fields are required"},status=400)
            db=Urlshorten.objects.create(Short_url=short,Long_url=long)
            return JsonResponse({"Message":"URL SUccefuuly inserted"},status=200)
        except Exception as e:
            return JsonResponse({"Message":"Something went wrong"},status=500)
    return JsonResponse({"Messahe":"Method not found"},status=405)

def get_url(request):
    if request.method=="GET":
        try:
            db=Urlshorten.objects.all().values("Short_url","Long_url","Created_at")
            data=list(db)
            if not data:
                return JsonResponse({"Messahe":"Fields are Empty"},status=400)
            return JsonResponse({"data":data},status=200)

        except Exception as e:
            return JsonResponse({"Message":"Something went wrong"},status=500)
    return JsonResponse({"Messahe":"Method not found"},status=405)
