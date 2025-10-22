from rest_framework import serializers

class LeaderboardEntrySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    score = serializers.IntegerField()