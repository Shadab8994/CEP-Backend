# from django.urls import path
# from .views import event_list

# urlpatterns = [
#     path('', event_list, name='event_list'),
# ]

# from django.urls import path
# from .views import event_list, registered_list

# urlpatterns = [
#     path('', event_list, name='event_list'),
#     path('registered/', registered_list, name='registered_list'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.event_list, name='home'),
#     path('register/', views.register_event, name='register'),
#     path('feedback/', views.feedback_view, name='feedback'),
#     path('registered/', views.registered_list, name='registered'),  
#     path('register/', views.register_event, name='register'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='home'),
    path('registered/', views.registered_list, name='registered'),
    path('feedback/', views.feedback_view, name='feedback'),
]