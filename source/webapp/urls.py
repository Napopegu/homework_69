from django.urls import path
from webapp.views import  add_view, subtract_view, multiply_view, divide_view, get_token_view,index


urlpatterns = [
    path('', index, name='index'),
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide'),
    path('token/', get_token_view, name='get_token')
]