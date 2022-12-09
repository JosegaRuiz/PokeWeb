from django.urls import path
from . import views
from rest_framework import routers

from .viewsets import TypeViewSet

router = routers.SimpleRouter()
router.register('types', TypeViewSet)

urlpatterns = router.urls
#urlpatterns = [
#    path('', views.index, name='index'),
#]