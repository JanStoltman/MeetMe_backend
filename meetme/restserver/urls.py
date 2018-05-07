from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken import views as authViews
from rest_framework import routers

from .views import *

router =routers.DefaultRouter()
router.register(r'Events', Events, base_name='Events')
router.register(r'Users', MeetUsers, base_name='Users')

app_name = 'restserver'
urlpatterns = [
    url(r'^', include(router.urls))
]

