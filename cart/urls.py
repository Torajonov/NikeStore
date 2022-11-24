from django.urls import path
from .import views

app_name  = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/', views.addToCart, name='add'),
    path('delete/<int:product_id>/<int:qty>', views.delete_item, name='delete'),
    path('remove/', views.remove , name='remove'),
    path('order/add/<int:cart_id>', views.addOrder, name='order_add'),
    path('order/done/', views.orderDone, name='order_done'),
]
