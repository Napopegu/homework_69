from django.shortcuts import render
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseNotAllowed,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView



@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method =='GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])

def index(request):
    return render(request, 'index.html')

class Index(TemplateView):
    template_name = 'index.html'


def perform_operation(request, operation):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            A = float(data.get('A'))
            B = float(data.get('B'))

            if operation == 'add':
                result = A + B
            elif operation == 'subtract':
                result = A - B
            elif operation == 'multiply':
                result = A * B
            elif operation == 'divide':
                if B != 0:
                    result = A / B
                else:
                    return JsonResponse({'error': 'Division by zero!'}, status=400)

            return JsonResponse({'answer': result})

        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid input data. A and B must be numbers.'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def add_view(request, *args, **kwargs):
    return perform_operation(request, 'add')

def subtract_view(request, *args, **kwargs):
    return perform_operation(request, 'subtract')

def multiply_view(request, *args, **kwargs):
    return perform_operation(request, 'multiply')

def divide_view(request, *args, **kwargs):
    return perform_operation(request, 'divide')

