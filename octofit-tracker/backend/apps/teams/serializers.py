from rest_framework import serializers
from .models import Team, TeamActivity


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'created_at']


class TeamActivitySerializer(serializers.ModelSerializer):
    team = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = TeamActivity
        fields = ['id', 'team', 'activity_name', 'date', 'duration']
