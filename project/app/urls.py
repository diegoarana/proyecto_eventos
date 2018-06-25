from django.conf.urls import url, include
from rest_framework import routers
from .views import QuestionViewSet, ChoiceViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet, base_name='question')
router.register(r'choice', ChoiceViewSet, base_name='choice')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
]
