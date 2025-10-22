from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    # Djongo uses ObjectIdField named `_id`; expose it as 'id' for the API
    id = serializers.CharField(source='_id', read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'name', 'duration', 'distance', 'date']
