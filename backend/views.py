from django.http import JsonResponse


# Create your views here.
def data(request):
    return JsonResponse(data={"data": {"title": "Hello World"}}, status=200)
