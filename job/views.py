
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions

from company.models import Company
from user.permissions import IsEmployer

from .models import Job
from .serializers import JobSerializer


class JobListView(generics.ListAPIView):
    queryset = Job.objects.filter(status='open')
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'location']
    search_fields = ['title', 'description']


#  create job 
class JobCreateView(generics.CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):
        company = Company.objects.get(employer=self.request.user)
        serializer.save(company=company)


# edit/close own job only

class JobUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get_queryset(self):
        return Job.objects.filter(company__employer=self.request.user)


# Employer dashboard

class EmployerDashboardView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get_queryset(self):
        return Job.objects.filter(company__employer=self.request.user)
