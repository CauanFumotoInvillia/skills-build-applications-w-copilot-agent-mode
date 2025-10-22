from rest_framework import viewsets
from .models import LeaderboardEntry
from .serializers import LeaderboardEntrySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer

    def get_queryset(self):
        # Optionally filter the queryset based on request parameters
        queryset = super().get_queryset()
        # Add any filtering logic here if needed
        return queryset