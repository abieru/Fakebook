from django.urls import path
from .views import SignUpView, ProfileUpdate

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='register'),
	path('profile/', ProfileUpdate.as_view(), name='profile'),
]