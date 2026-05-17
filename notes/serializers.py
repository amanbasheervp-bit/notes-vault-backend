from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'email': {'required': False}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
        )
        return user


class NoteSerializer(serializers.ModelSerializer):
    tags_list = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Note
        fields = (
            'id', 'title', 'content', 'tags', 'tags_list',
            'category', 'is_pinned', 'owner',
            'created_at', 'updated_at',
        )
        read_only_fields = ('id', 'owner', 'tags_list', 'created_at', 'updated_at')
