"""IS_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    # hxx
    path('', views.home),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user_profile/', views.user_profile),
    path('login/', views.login),
    path('error/', views.error),
    path('department_management/', views.department_management),
    path('employee_management/', views.employee_management),
    path('sales_management/', views.sales_orders),
    path('add_sales_order_management/', views.add_sales_order_management),
    path('edit_sales_order_management/', views.edit_sales_order_management),
    path('delete_sales_order_management/', views.delete_sales_order_management),

    # wh
    path('wuliu/', views.wuliu),
    path('wuliu_time/', views.wuliu_time),
    path('wuliu_map/', views.wuliu_mapp),
    path('orm/', views.orm),

    # zwx
    path('purchase_department/', views.purchase_department),
    # path('purchase_department/show/', views.purchase_department_show),
    path('GYS_add/', views.GYS_add),
    path('GYS_show/', views.GYS_show),
    path('GYS_edit/', views.GYS_edit),
    path('GYS_delete/', views.GYS_delete),
    path('details_purchase/', views.details_purchase),
    path('purchase_orders_show/', views.purchase_orders_show),
    path('purchase_orders_make/', views.purchase_orders_make),
    path('purchase_orders_delete/', views.purchase_orders_delete),
    path('purchase_orders_add/', views.purchase_orders_add),
    path('purchase_orders_edit/', views.purchase_orders_edit),

    # xjl
    # 财务部门
    path('purchase_orders/', views.purchase_orders),
    path('add_purchase_order/', views.add_purchase_order),
    path('edit_purchase_order/', views.edit_purchase_order),
    path('delete_purchase_order/', views.delete_purchase_order),
    path('edit_purchase_order2/', views.edit_purchase_order2),
    path('purchase_order_detail/', views.purchase_order_detail),  # 新增功能1
    path('sales_orders/', views.sales_orders),
    path('add_sales_order/', views.add_sales_order),
    path('edit_sales_order/', views.edit_sales_order),
    path('delete_sales_order/', views.delete_sales_order),
    path('make_invoice/', views.make_invoice),
    path('sales_order_detail/', views.sales_order_detail),
    path('income_manage/', views.income_manage),
    path('expenditure_manage/', views.expenditure_manage),
    path('purchase_order_payoff/', views.purchase_order_payoff),
    # 库存部门
    path('receipt_confirm/', views.receipt_confirm),
    path('storage_details/', views.storage_details),
    path('edit_storage/', views.edit_storage),
    path('purchase_order_confirm/', views.purchase_order_confirm),
    path('warehouse_manage/', views.warehouse_manage),
    path('ex_warehouse/', views.ex_warehouse),

    #hq
    path('page_kf/', views.page_kf),
    path('page_kf/wuliu_search', views.to_wuliu),
    path('page_kf/suyuan', views.suyuan_search),
    path('page_kf/suyuan/suyuan_details/', views.suyuan_details)

]


urlpatterns += staticfiles_urlpatterns()