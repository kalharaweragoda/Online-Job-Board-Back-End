from django.urls import path

from .views import JobListView, JobCreateView, JobUpdateView, EmployerDashboardView

urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('create/', JobCreateView.as_view(), name='job-create'),
    path('<int:pk>/', JobUpdateView.as_view(), name='job-update'),
    path('dashboard/', EmployerDashboardView.as_view(), name='employer-dashboard'),
]