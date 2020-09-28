from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.users.api.serializers import UserSerializer


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data)
