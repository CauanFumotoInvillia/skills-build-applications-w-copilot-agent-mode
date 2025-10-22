
from rest_framework import viewsets
from .models import Team, TeamActivity
from .serializers import TeamSerializer, TeamActivitySerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamActivityViewSet(viewsets.ModelViewSet):
    queryset = TeamActivity.objects.all()
    serializer_class = TeamActivitySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        team = self.request.query_params.get('team')
        if team:
            queryset = queryset.filter(team__name=team)
        return queryset