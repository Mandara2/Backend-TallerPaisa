from django.urls import path, include
from rest_framework import routers
from apps.crud.views.managerView import ManagerView

router = routers.DefaultRouter()
router.register(r'', ManagerView, 'manager')

urlpatterns = [
    path('', include(router.urls))
]