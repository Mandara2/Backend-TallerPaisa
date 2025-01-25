from django.urls import path, include
from rest_framework import routers
from apps.crud.views.departmentView import DepartmentView

router = routers.DefaultRouter()
router.register(r'', DepartmentView, 'department')

urlpatterns = [
    path('', include(router.urls))
]