from django.urls import path

from apps.api.views import ToDoList, ToDoDetail, UserDetail, UserList

app_name = 'api'
urlpatterns = [
    path('', ToDoList.as_view(), name='list'),
    path('<int:pk>', ToDoDetail.as_view(), name='detail'),
    # path('<slug:slug>/update/', ToDoUpdate.as_view(),name ='update'),
    # path('<slug:slug>/delete', ToDoDelete.as_view(),name ='delete'),

    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
]
