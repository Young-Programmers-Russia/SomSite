from rest_framework import serializers
from .models import Launcher


class LauncherSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Launcher
        fields = ['version', 'file_url']

    def to_representation(self, instance):
        file_url = self.fields['file_url']
        file_url_value = file_url.to_representation(file_url.get_attribute(instance))
        return {
            'last-version': instance.version,
            'download-url': file_url_value
        }
    
    def get_file_url(self, launcher):
        request = self.context.get('request')
        file_url = launcher.file.url
        return request.build_absolute_uri(str(file_url))

