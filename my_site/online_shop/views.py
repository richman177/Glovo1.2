from rest_framework import viewsets, generics, status
from .models import *
from .permissions import CheckOrder, UpdateCourier, CheckOwner, CreateReview, CheckStatus
from .serializers import *
from .filters import StoreFilter, ProductFilter, ComboFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import  IsAuthenticatedOrReadOnly


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StoreFilter
    search_fields = ['store_name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class StoreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StoreImageViewSet(viewsets.ModelViewSet):
    queryset = StoreImage.objects.all()
    serializer_class = StoreImageSerializer


class StoreCreateAPIView(generics.CreateAPIView):
    serializer_class = StoreSerializer
    permission_classes = [CheckOwner] #CheckStatus]


class StoreEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [CheckOwner]


class Contact_InfoViewSet(viewsets.ModelViewSet):
    queryset = Contact_Info.objects.all()
    serializer_class = Contact_InfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckOwner]


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['Product_name']
    ordering_fields = ['price']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckOwner, CheckStatus]


class ProductEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckOwner, CheckStatus]


class ComboProductListAPIView(generics.ListAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ComboFilter
    search_fields = ['combo_name']
    ordering_fields = ['combo_price']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ComboProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckOwner]


class ComboProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ComboProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckOwner, CheckStatus]


class ComboProductEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckOwner, CheckStatus]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class OrderListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckOrder, UpdateCourier]


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckOrder, UpdateCourier, CheckOwner]


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourierListAPIView(generics.ListAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourierDetailAPIView(generics.RetrieveAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StoreReviewViewSet(viewsets.ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CreateReview]


class CourierReviewViewSet(viewsets.ModelViewSet):
    queryset = CourierReview.objects.all()
    serializer_class = CourierReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CreateReview]
