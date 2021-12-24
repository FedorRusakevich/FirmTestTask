from rest_framework import serializers

from .models import *


class EmployeesList(serializers.ModelSerializer):

    head_name = serializers.SlugRelatedField(slug_field="name", read_only=True)
    position = serializers.SlugRelatedField(slug_field="position", read_only=True)
    level = serializers.SlugRelatedField(slug_field="level", read_only=True)

    class Meta:
        model = Employees
        fields = "__all__"
