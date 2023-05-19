from functools import wraps
from time import time
import requests

def speed_test(fn):
    wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        fn(*args, **kwargs)
        end_time = time()
        runtime = end_time - start_time
        print(f"Function's '{fn.__name__}', with given parameters {args} runtime: {round(runtime, 2)}s")
    return wrapper

@speed_test
def get_status(website):
    r = requests.get(website)
    print(r.status_code)

get_status('http://python.org')
@speed_test
def prime_finder(given_range):
    final_list = []
    for num in range(given_range):
        if num > 1:
            for i in range(2,num):
                    if (num % i) == 0:
                        break
            else:
                final_list.append(num)
    return final_list
prime_finder(10000)