from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ImageViewSet, RegisterView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'images', ImageViewSet, basename='image')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
