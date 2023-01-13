from rest_framework.routers import SimpleRouter
from django.urls import path, include
from user.views import RegisterAPIView, AuthView

app_name = "user"
router = SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path("register/", RegisterAPIView.as_view()), #회원가입
    path("auth/", AuthView.as_view()), #로그인
]