from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

# Output serializer for user
class UserSimpleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = ['id', 'name']

# Input serializer for user (used in POST input)
class UserInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)  # Optional, for structure only

# Output serializer for project inside client detail
class ProjectSimpleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='project_name')  # Rename for output

    class Meta:
        model = Project
        fields = ['id', 'name']

# GET /clients/ list view
class ClientListSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']

# GET /clients/:id detail view
class ClientDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = ProjectSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at', 'projects']

# Final Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    client = serializers.StringRelatedField(read_only=True)

    users = UserSimpleSerializer(many=True, read_only=True)  # Output
    users_input = UserInputSerializer(many=True, write_only=True, source='users')  # Input

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users_input', 'users', 'created_at', 'created_by']

    def create(self, validated_data):
        users_data = validated_data.pop('users')
        project = Project.objects.create(**validated_data)

        user_ids = [u['id'] for u in users_data if 'id' in u]
        users = User.objects.filter(id__in=user_ids)

        if users.count() != len(user_ids):
            raise serializers.ValidationError("One or more user IDs are invalid.")

        project.users.set(users)
        return project






