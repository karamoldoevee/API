from django.contrib import admin
from django.urls import path
from webapp.views import api_add, api_subtract, api_multiply, api_divide, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add/', api_add, name='add'),
    path('subtract/', api_subtract, name='subtract'),
    path('multiply/', api_multiply, name='multiply'),
    path('divide/', api_divide, name='divide'),
]