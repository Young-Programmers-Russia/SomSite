from rest_framework import serializers
from .models import Mod


class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mod
        fields = ['mod_id', 'mod_name', 'mod_link', 'sha1']
