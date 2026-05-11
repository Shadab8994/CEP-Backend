from django.urls import path
from .views import event_list

urlpatterns = [
    path('', event_list, name='event_list'),
]

from django.urls import path
from .views import event_list, registered_list

urlpatterns = [
    path('', event_list, name='event_list'),
    path('registered/', registered_list, name='registered_list'),
]