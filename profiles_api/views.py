from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers
from .models import models
from rest_framework.authentication import TokenAuthentication
from .permissions import permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function",
            "is similiar to a traditional Django view",
            "Gives you the most control over your application logic",
            "is mapped manually to URLs",
        ]

        return Response({"message": "Hello world!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Handles object deletion"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""

        a_viewset = [
            "Users action (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handle getting a single object by its id"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """handle updating a single object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """handle updating part of a single object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """handle removing an object"""
        return Response({"http_method": "DELETE"})


class UserProfileviewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = permissions.UpdateOwnProfile
