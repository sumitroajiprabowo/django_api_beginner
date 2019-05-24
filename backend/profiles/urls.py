from django.urls import path, include

from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewset, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]