from django.urls import path
from .views import list_users, create_user, update_user, delete_user,create_phone, create_email,query,error

urlpatterns = [
    path('', list_users, name='list_users'),
    path('new', create_user, name='create_user'),
    path('update/<int:id>', update_user, name='update_user'),
    path('delete/<int:id>', delete_user, name='delete_user'),
    path('newphone/<int:id>', create_phone, name='create_phone'),
    path('newmail/<int:id>', create_email, name='create_email'),
    path('search/', query, name='query'),
    path('error/', error, name='error'),
]