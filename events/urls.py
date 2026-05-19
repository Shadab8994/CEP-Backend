

# from django.urls import path
# from . import views


# urlpatterns = [
#     path('', views.event_list, name='home'),
#     path('registered/', views.registered_list, name='registered'),
#     path('feedback/', views.feedback_view, name='feedback'),

#     path('signup/', views.signup_view, name='signup'),
#     path('login/', views.login_view, name='login'),
#     path('view-feedback/', views.view_feedbacks, name='view_feedbacks'),
#     path('logout/', views.logout_view, name='logout'),
#     path('add-event/', views.add_event, name='add_event'),
#     path('edit-event/<int:event_id>/', views.edit_event, name='edit_event'),
#     path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
#     path('api/events/', views.event_api),
#     path('api/add-event/', views.add_event_api),
#     path('api/update-event/<int:event_id>/',views.update_event_api),
#     path('event/<int:event_id>/',views.event_detail,name='event_detail'),
#     path('change-username/',views.change_username,name='change_username'),
#     path('change-password/',views.change_password,name='change_password'),
# ]

from django.urls import path
from . import views

urlpatterns = [

    #  Home
    path('', views.event_list, name='home'),

    #  Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    #  Event Pages
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('add-event/', views.add_event, name='add_event'),
    path('edit-event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),

    #  Registration & Feedback
    path('registered/', views.registered_list, name='registered'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('view-feedback/', views.view_feedbacks, name='view_feedbacks'),

    #  Profile
    path('change-username/', views.change_username, name='change_username'),
    path('change-password/', views.change_password, name='change_password'),

    #  APIs
    path('api/events/', views.event_api),
    path('api/add-event/', views.add_event_api),
    path('api/update-event/<int:event_id>/', views.update_event_api),
]