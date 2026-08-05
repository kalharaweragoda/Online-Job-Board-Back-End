from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings as django_settings
from .models import Application
from .serializers import ApplicationSerializer, ApplicationStatusUpdateSerializer
from user.permissions import IsJobSeeker, IsEmployer


# Job Seeker: apply to a job
class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsJobSeeker]

    def perform_create(self, serializer):
        application = serializer.save(applicant=self.request.user)

        # Email notification (business logic + Section 4.5 requirement)
        try:
            send_mail(
                subject='Application Submitted',
                message=f'You applied for {application.job.title}.',
                from_email=django_settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.request.user.email],
                fail_silently=True,
            )
            send_mail(
                subject='New Applicant',
                message=f'{self.request.user.username} applied for {application.job.title}.',
                from_email=django_settings.DEFAULT_FROM_EMAIL,
                recipient_list=[application.job.company.employer.email],
                fail_silently=True,
            )
        except Exception:
            pass


# Job Seeker: view own applications
class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsJobSeeker]

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)


# Employer: view applicants for own jobs
class JobApplicantsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return Application.objects.filter(job_id=job_id, job__company__employer=self.request.user)


  # update applicant status
  
class ApplicationStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ApplicationStatusUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get_queryset(self):
        return Application.objects.filter(job__company__employer=self.request.user)

    def perform_update(self, serializer):
        application = serializer.save()
        
        # Notify job seeker of status change
        
        try:
            send_mail(
                subject='Application Status Updated',
                message=f'Your application for {application.job.title} is now: {application.status}',
                from_email=django_settings.DEFAULT_FROM_EMAIL,
                recipient_list=[application.applicant.email],
                fail_silently=True,
            )
        except Exception:
            pass