from django.urls import path, include
from rest_framework import routers
from apps.crud.views.installmentView import InstallmentView

router = routers.DefaultRouter()
router.register(r'', InstallmentView, 'installment')

urlpatterns = [
    path('', include(router.urls))
]