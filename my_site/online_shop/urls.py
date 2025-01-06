from django.urls import path, include
from.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contact', Contact_InfoViewSet, basename='contacts'),
router.register(r'cart', CartViewSet, basename='carts'),
router.register(r'cart_item', CartItemViewSet, basename='cart_items'),
router.register(r'store_review', StoreReviewViewSet, basename='store_reviews'),
router.register(r'courier_review', CourierReviewViewSet, basename='courier_reviews'),

urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),
    path('store/create/', StoreCreateAPIView.as_view(), name='store_create'),
    path('store/create/<int:pk>/', StoreEDITAPIView.as_view(), name='store_edit'),
    path('products/', ProductListAPIView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='products_detail'),
    path('products/create/', ProductCreateAPIView.as_view(), name='products_create'),
    path('products/create/<int:pk>/', ProductEDITAPIView.as_view(), name='products_edit'),
    path('orders/', OrderListAPIView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='orders_detail'),
    path('combo_product/', ComboProductListAPIView.as_view(), name='combo_product_list'),
    path('combo_product/<int:pk>/', ComboProductListAPIView.as_view(), name='combo_product_detail'),
    path('combo_product/create/', ComboProductCreateAPIView.as_view(), name='combo_product_create'),
    path('combo_product/create/<int:pk>/', ComboProductEDITAPIView.as_view(), name='combo_product_edit'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('courier/', CourierListAPIView.as_view(), name='courier_list'),
    path('courier/<int:pk>/', CourierDetailAPIView.as_view(), name='courier_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
]
