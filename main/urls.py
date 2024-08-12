from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('default-dashboard/', views.default_dashboard, name='default_dashboard'),
    path('logout/', logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('analyst_dashboard/', views.analyst_dashboard, name='analyst_dashboard'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.group_create, name='group_create'),
    path('groups/<int:group_id>/edit/', views.group_update, name='group_update'),
    path('groups/<int:group_id>/delete/', views.group_delete, name='group_delete'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/create/', views.ticket_create, name='ticket_create'),
    path('tickets/<int:ticket_id>/', views.ticket_delete, name='ticket_confirm_delete'),
    path('tickets/<int:ticket_id>/edit/', views.ticket_update, name='ticket_update'),
    path('tickets/<int:ticket_id>/delete/', views.ticket_delete, name='ticket_delete'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/update/', views.user_update, name='user_update'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
]
