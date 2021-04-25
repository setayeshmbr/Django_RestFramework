from django.contrib.auth.models import User
from rest_framework import serializers

from apps.blog.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        # fields = ['title','content','status','slug','author','publish']
        # fields = '__all__'  # returns all model fields
        exclude = ['created', 'updated']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['title','content','status','slug','author','publish']
        fields = '__all__'  # returns all model fields
        # exclude =['created','updated']
