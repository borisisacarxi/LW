from django.urls import path, include
from users.views import index

urlpatterns = [
    path('', index, name='index'),
]