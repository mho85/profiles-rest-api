from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register(r'profiles', views.UserProfileViewSet)
router.register(r'feeds', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls))
]
