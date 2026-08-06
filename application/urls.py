from django.urls import path

from .views import (
    ApplicationCreateView,
    ApplicationStatusUpdateView,
    JobApplicantsView,
    MyApplicationsView,
)

urlpatterns = [
    path('', ApplicationCreateView.as_view(), name='application-create'),
    path('me/', MyApplicationsView.as_view(), name='my-applications'),
    path('job/<int:job_id>/', JobApplicantsView.as_view(), name='job-applicants'),
    path('<int:pk>/status/', ApplicationStatusUpdateView.as_view(), name='application-status-update'),
]