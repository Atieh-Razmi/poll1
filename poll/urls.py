from django.urls import path, include
from rest_framework import routers
from .views import PollViewSet
from rest_framework.authtoken import views

router = routers.SimpleRouter()
router.register(r'polls', PollViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', views.obtain_auth_token)
]


