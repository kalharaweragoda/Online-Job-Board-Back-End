from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Job
        fields = [
            'id', 'company', 'company_name', 'category', 'title', 'description',
            'location', 'salary_min', 'salary_max', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['company']