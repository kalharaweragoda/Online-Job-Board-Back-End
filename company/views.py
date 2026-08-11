from rest_framework import generics, permissions
from .models import Company
from .serializers import CompanySerializer
from user.permissions import IsEmployer


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)


class CompanyDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get_queryset(self):
        return Company.objects.filter(employer=self.request.user)

    def get_object(self):
        return self.get_queryset().get()