import datetime


def solution(lines):

    interval = []

    for i in range(len(lines)):

        a, b, c = lines[i].split()
        dt = a + ' ' + b
        response_time = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S.%f")
        request_time = response_time - datetime.timedelta(seconds=float(c[:-1])-0.001)
        str_req = datetime.datetime.strftime(request_time, "%Y-%m-%d %H:%M:%S.%f")
        str_res = datetime.datetime.strftime(response_time, "%Y-%m-%d %H:%M:%S.%f")

        before_request = request_time - datetime.timedelta(seconds=0.999)
        after_request = request_time + datetime.timedelta(seconds=0.999)
        before_response = response_time - datetime.timedelta(seconds=0.999)
        after_response = response_time + datetime.timedelta(seconds=0.999)

        before_req = datetime.datetime.strftime(before_request, "%Y-%m-%d %H:%M:%S.%f")
        after_req = datetime.datetime.strftime(after_request, "%Y-%m-%d %H:%M:%S.%f")
        before_res = datetime.datetime.strftime(before_response, "%Y-%m-%d %H:%M:%S.%f")
        after_res = datetime.datetime.strftime(after_response, "%Y-%m-%d %H:%M:%S.%f")

        interval.extend([(before_req, str_req), (str_req, after_req), (before_res, str_res), (str_res, after_res)])
        lines[i] = (str_req, str_res)

    included = [0] * len(interval)
    for i in range(len(lines)):
        req, res = lines[i]

        for j in range(len(interval)):
            start, end = interval[j]
            if res < start or req > end:
                continue
            else:
                included[j] += 1

    # print(included)

    return max(included)


print(solution(["2016-09-15 23:59:59.999 0.001s"]))
