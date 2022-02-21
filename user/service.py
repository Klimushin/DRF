from user.models import DataForEmail


request_time = []


# def count_call_endpoint():
#     global initial_count
#     initial_count += 1
#     request_count = initial_count
#     print(request_count)
#     return request_count


def average_request_time(total_time):
    global request_time
    request_time.append(total_time)
    average_time = sum(request_time) / len(request_time)
    request_count = len(request_time)
    if DataForEmail.objects.first():
        DataForEmail.objects.update(average_time=average_time, request_count=request_count)
    else:
        DataForEmail.objects.create(average_time=average_time, request_count=request_count)
    print(average_time)
    print(request_count)
    return average_time
