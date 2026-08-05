from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    applicant_name = serializers.CharField(source='applicant.username', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'job', 'job_title', 'applicant', 'applicant_name', 'status', 'cover_letter', 'applied_at']
        read_only_fields = ['applicant', 'status']


class ApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']