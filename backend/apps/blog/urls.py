
from django.urls import path

from apps.blog.views import ToDoList, ToDoDetail, UserDetail, UserList

app_name= 'blog'
urlpatterns = [
    path('', ToDoList.as_view(),name ='list'),
    path('<int:pk>', ToDoDetail.as_view(),name ='detail'),


    path('users/', UserList.as_view(),name ='user-list'),
    path('users/<int:pk>', UserDetail.as_view(),name ='user-detail'),
]