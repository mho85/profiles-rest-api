from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'returns HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional Django view',
            'gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """Fully updates a object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Partially updates a object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deletes a object"""
        return Response({'method': 'DELETE'})
