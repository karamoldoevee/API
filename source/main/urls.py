from django.contrib import admin
from django.urls import path
from webapp.views import api_add


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', api_add, name='add'),
]
