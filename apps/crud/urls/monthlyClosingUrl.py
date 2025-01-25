from django.urls import path, include
from rest_framework import routers
from apps.crud.views.monthlyClosingView import MonthlyClosingView

router = routers.DefaultRouter()
router.register(r'', MonthlyClosingView, 'monthlyClosing')

urlpatterns = [
    path('', include(router.urls))
]