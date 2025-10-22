
from rest_framework.views import APIView
from rest_framework.response import Response

class TeamListView(APIView):
    def get(self, request):
        return Response({'message': 'Team list endpoint stub'})

class TeamCreateView(APIView):
    def post(self, request):
        return Response({'message': 'Team create endpoint stub'})

class TeamDetailView(APIView):
    def get(self, request, pk):
        return Response({'message': f'Team detail endpoint stub for id {pk}'})

class TeamUpdateView(APIView):
    def put(self, request, pk):
        return Response({'message': f'Team update endpoint stub for id {pk}'})

class TeamDeleteView(APIView):
    def delete(self, request, pk):
        return Response({'message': f'Team delete endpoint stub for id {pk}'})