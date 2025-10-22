
from rest_framework.views import APIView
from rest_framework.response import Response

class ActivityListView(APIView):
    def get(self, request):
        return Response({'message': 'Activity list endpoint stub'})

class ActivityDetailView(APIView):
    def get(self, request, pk):
        return Response({'message': f'Activity detail endpoint stub for id {pk}'})