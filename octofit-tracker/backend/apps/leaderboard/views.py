from rest_framework.views import APIView
from rest_framework.response import Response

class LeaderboardStubView(APIView):
    def get(self, request):
        return Response({'message': 'Leaderboard endpoint stub'})
from rest_framework import viewsets
from .models import LeaderboardEntry
from .serializers import LeaderboardEntrySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        team = self.request.query_params.get('team')
        if team:
            queryset = queryset.filter(user__team__name=team)
        return queryset