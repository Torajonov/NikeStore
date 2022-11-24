from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.HomePageView.as_view() , name='home'),
    path('detail/<pk>',views.ProductDetailView.as_view(),name='product_detail'),

    path('category/<slug:category_slug>/', views.categoryDetail,name='category_detail'),
    path('tag/<slug:tag_slug>/', views.tagDetail,name='tag_detail'),

    path('accounts/profile/', views.profile, name='profile'),
    path('search/', views.liveSearch, name='search')
]
