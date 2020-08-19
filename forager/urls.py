from django.urls import path, include
from . import views
from rest_framework import routers
from .views import current_user, UserList

router = routers.DefaultRouter()
router.register('plants', views.PlantView)
router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('current_user/', current_user),
    path('users', UserList.as_view()),
]