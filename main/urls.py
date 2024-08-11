from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Додайте цей рядок для кореневого шляху
    path('home/', views.home, name='home'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.group_create, name='group_create'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('groups/<int:group_id>/update/', views.group_update, name='group_update'),
    path('groups/<int:group_id>/delete/', views.group_delete, name='group_delete'),

    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/create/', views.ticket_create, name='ticket_create'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/<int:ticket_id>/update/', views.ticket_update, name='ticket_update'),
    path('tickets/<int:ticket_id>/delete/', views.ticket_delete, name='ticket_delete'),

    path('users/', views.user_list, name='user_list'),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('analyst_dashboard/', views.analyst_dashboard, name='analyst_dashboard'),
    path('default_dashboard/', views.default_dashboard, name='default_dashboard'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
