from rest_framework.views import APIView
from rest_framework.response import Response

class HellowWorld(APIView):
  def get(self, request):
    return Response('HELLO WORLD! from Django.')