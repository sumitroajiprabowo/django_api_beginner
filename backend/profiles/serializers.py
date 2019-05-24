
from rest_framework import serializers

from . import models



class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfiles
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfiles.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user