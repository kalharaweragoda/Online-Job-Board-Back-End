
from rest_framework import generics, permissions

from user.permissions import IsEmployer

from .models import Company
from .serializers import CompanySerializer


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)   # business logic: link to logged-in employer


class CompanyDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get_queryset(self):
        return Company.objects.filter(employer=self.request.user)   # can only see/edit own company