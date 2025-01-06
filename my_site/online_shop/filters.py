from django_filters import FilterSet
from .models import Store, Product, ComboProduct


class StoreFilter(FilterSet):
    class Meta:
        model = Store
        fields = {
            'category': ['exact'],
        }

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt']
        }

class ComboFilter(FilterSet):
    class Meta:
        model = ComboProduct
        fields = {
            'combo_price': ['gt', 'lt']
        }
