# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from apps.blog.models import ToDo


class ToDoList(ListView):
    def get_queryset(self):
        return ToDo.objects.filter(status=True)


class ToDoDetail(DetailView):
    def get_object(self, queryset=None):
        return get_object_or_404(ToDo, pk=self.kwargs.get('pk'))


class UserList(ListView):
    def get_queryset(self):
        return User.objects.all()


class UserDetail(DetailView):
    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))
