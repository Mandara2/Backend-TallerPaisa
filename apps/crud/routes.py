from django.urls import path, include

urlpatterns = [
    path('address/', include('apps.crud.urls.addressUrl')),
    path('branch/', include('apps.crud.urls.branchUrl')),
    path('category/', include('apps.crud.urls.categoryUrl')),
    path('city/', include('apps.crud.urls.cityUrl')),
    path('customer/', include('apps.crud.urls.customerUrl')),
    path('dailyClosing/', include('apps.crud.urls.dailyClosingUrl')),
    path('department/', include('apps.crud.urls.departmentUrl')),
    path('employee/', include('apps.crud.urls.employeeUrl')),
    path('installment/', include('apps.crud.urls.installmentUrl')),
    path('invoice/', include('apps.crud.urls.invoiceUrl')),
    path('manager/', include('apps.crud.urls.managerUrl')),
    path('monthlyClosing/', include('apps.crud.urls.monthlyClosingUrl')),
    path('order/', include('apps.crud.urls.orderUrl')),
    path('product/', include('apps.crud.urls.productUrl')),
    path('sale/', include('apps.crud.urls.saleUrl')),
    path('shoppingCart/', include('apps.crud.urls.shoppingCartUrl')),
    path('supplier/', include('apps.crud.urls.supplierUrl')),
]