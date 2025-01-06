from .models import Product, Store, Category, ComboProduct
from modeltranslation.translator import TranslationOptions,register


@register(Store)
class ProductTranslationOptions(TranslationOptions):
    fields = ('store_name', 'description', 'address')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')


@register(ComboProduct)
class ProductComboTranslationOptions(TranslationOptions):
    fields = ('combo_name', 'description')
