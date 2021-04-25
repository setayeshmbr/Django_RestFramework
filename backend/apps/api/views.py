# Create your views here.
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import ToDoSerializer, UserSerializer

from .permissions import IsSuperUser, IsAuthorOrReadOnly ,IsSuperUserOrStaffReadOnly
from ..blog.models import ToDo


class ToDoList(ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class ToDoDetail(RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    # lookup_field = 'slug'


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

#
# class ToDoDetail(RetrieveAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#     lookup_field = 'slug'
#
#
# class ToDoUpdate(UpdateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#     lookup_field = 'slug'
#
#
# class ToDoDelete(DestroyAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#     lookup_field = 'slug'
