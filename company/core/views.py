from rest_framework import viewsets, generics
from .models import Client, Project
from .serializers import ClientListSerializer, ClientDetailSerializer, ProjectSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ClientListSerializer
        elif self.action == 'retrieve':
            return ClientDetailSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ClientListSerializer  # ✅ cleaner output without projects/updated_at
        return ClientListSerializer

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else User.objects.get(username='Rohit')
        serializer.save(created_by=user)

    def perform_update(self, serializer):
        serializer.save()

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user if self.request.user.is_authenticated else User.objects.get(username='Ganesh')
        return Project.objects.all()  # ✅ returns all projects (not filtered by user)

class ClientProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        client = get_object_or_404(Client, id=self.kwargs['client_id'])
        user = self.request.user if self.request.user.is_authenticated else User.objects.get(username='Ganesh')
        serializer.save(client=client, created_by=user)




