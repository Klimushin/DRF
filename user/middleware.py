import time
from api.viewsets import count_call_endpoint, average_request_time


def timing(get_response):
    def middleware(request):
        if request.path == '/api/employees/':
            count_call_endpoint()
            t1 = time.time()
            response = get_response(request)
            t2 = time.time()
            average_request_time(t2 - t1)
            return response
        else:
            response = get_response(request)
            return response
    return middleware
