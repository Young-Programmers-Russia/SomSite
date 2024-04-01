from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label='username',
        write_only=True
    )
    password = serializers.CharField(
        label='password',
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password
            )
            if not user:
                message = 'Access denied: wrong username or password'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs


class RegistrationSerializer(serializers.Serializer):
    ...
