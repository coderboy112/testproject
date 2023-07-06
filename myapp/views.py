from django.http import JsonResponse

def api_endpoint(request):
    return_msg=""
    for i in range(0,10):
        return_msg=return_msg+str(i)+" "
    return JsonResponse({"message":return_msg})

def api_endpoint1(request):
    return_msg = 'this is the required api for api2'
    return JsonResponse(return_msg, safe=False)