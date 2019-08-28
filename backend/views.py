from django.http import JsonResponse


# Create your views here.
def data(request):
    image_url = "https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1920,f_auto/A-Alamy-BXWK5E_vvmkuf.jpg"
    return JsonResponse(data={"data": {"image_url": image_url}}, status=200)
