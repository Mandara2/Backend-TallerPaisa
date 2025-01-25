from django.contrib import admin
from .models.address import Address
from .models.branch import Branch
from .models.category import Category
from .models.city import City
from .models.customer import Customer
from .models.dailyClosing import DailyClosing
from .models.department import Department
from .models.employee import Employee
from .models.installment import Installment
from .models.invoice import Invoice
from .models.manager import Manager
from .models.monthlyClosing import MonthlyClosing
from .models.order import Order
from .models.product import Product
from .models.purchase import Purchase
from .models.sale import Sale
from .models.shoppingCart import ShoppingCart
from .models.supplier import Supplier

# Register your models here.
admin.site.register([
    Address, Branch, Category, City, Customer, DailyClosing,
    Department, Employee, Installment, Invoice, Manager, MonthlyClosing,
    Order, Product, Purchase, Sale, ShoppingCart, Supplier
])
