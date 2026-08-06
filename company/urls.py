from django.urls import path

from .views import CompanyCreateView, CompanyDetailView

urlpatterns = [
    path('', CompanyCreateView.as_view(), name='company-create'),
    path('me/', CompanyDetailView.as_view(), name='company-detail'),
]