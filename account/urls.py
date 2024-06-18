from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, ActivationView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('profile/', UserProfileViewSet.as_view(({'get': 'list'})))
]