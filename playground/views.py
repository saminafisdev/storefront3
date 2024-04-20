from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView

# from .tasks import notify_customers
import requests
class HelloView(APIView):
    """
    Caching
    """

    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get("https://httpbin.org/delay/2")
        data = response.json()

        # return render(request, "hello.html", {"name": cache.get(key)})
        return render(request, "hello.html", {"name": data})
@cache_page(5 * 60)
def say_hello(request):
    # notify_customers.delay('Hello')

    # key = "httpbin_result"
    # if cache.get(key) is None:
    #     """
    #     Simulating a slow API endpoint
    #     """
    #     response = requests.get("https://httpbin.org/delay/2")
    #     data = response.json()
    #     print("-----------------")
    #     print(data)
    #     cache.set(key, data)

    response = requests.get("https://httpbin.org/delay/2")
    data = response.json()

    # return render(request, "hello.html", {"name": cache.get(key)})
    return render(request, "hello.html", {"name": data})
