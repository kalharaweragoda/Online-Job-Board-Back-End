from django.db import models

from user.models import User
from job.models import Job

class Application(models.Model):
    STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('reviewed', 'Reviewed'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='applied')
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"