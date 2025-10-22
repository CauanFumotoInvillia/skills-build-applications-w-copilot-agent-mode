from rest_framework import serializers
from .models import LeaderboardEntry


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'score', 'date']