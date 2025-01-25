from django.urls import path, include
from rest_framework import routers
from apps.crud.views.invoiceView import InvoiceView

router = routers.DefaultRouter()
router.register(r'', InvoiceView, 'invoice')

urlpatterns = [
    path('', include(router.urls))
]