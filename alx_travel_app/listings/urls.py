"""
URL configuration for listings app.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router for DRF viewsets (we'll add these later)
router = DefaultRouter()

urlpatterns = [
    # Include router URLs
    path('', include(router.urls)),
    
    # Add custom URL patterns here as needed
]