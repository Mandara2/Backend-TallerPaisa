from django.urls import path, include
from rest_framework import routers
from apps.crud.views.employeeView import EmployeeView

router = routers.DefaultRouter()
router.register(r'', EmployeeView, 'employee')

urlpatterns = [
    path('', include(router.urls))
]