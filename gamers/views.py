from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from gamers.models import Gamer
from gamers.serializers import GamerSerializer


@csrf_exempt
def gamer_list(request, version):
    if version == "v1":
        if request.method == 'GET':
            gamers = Gamer.objects.all().order_by('-score')
            serializer = GamerSerializer(gamers, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = GamerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse({'statue': 'error', 'msg': serializer.errors}, status=400)
    else:
        return JsonResponse({'status': 'error', 'msg': 'version is not defined'}, status=404)

@csrf_exempt
def gamer_detail(request, mobile, version):
    try:
        gamer = Gamer.objects.get(mobile=mobile)
    except Gamer.DoesNotExist:
        return JsonResponse({'status': 'error', 'msg': 'gamer does not found'}, status=404)

    if request.method == 'GET':
        serializer = GamerSerializer(gamer)
        return JsonResponse({'rank': serializer.data['rank']}, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        data['mobile'] = mobile
        serializer = GamerSerializer(gamer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=202)
        return JsonResponse({'statue': 'error', 'msg': serializer.errors}, status=400)

    elif request.method == 'DELETE':
        gamer.delete()
        return HttpResponse(status=202)