from django.urls import path, include
from rest_framework import routers
from apps.crud.views.dailyClosingView import DailyClosingView

router = routers.DefaultRouter()
router.register(r'', DailyClosingView, 'dailyClosing')

urlpatterns = [
    path('', include(router.urls))
]