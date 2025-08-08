from django.db import models 
from django.contrib.auth.models import  AbstractUser 
from phonenumber_field.modelfields import PhoneNumberField 
 

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('courier', 'Courier'),
        ('owner', 'Owner'),
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='client')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Store(models.Model):
    store_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='store_category')
    description = models.TextField()
    address = models.CharField(max_length=50)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.store_name} , {self.address}'

    class Meta:
        unique_together = ('owner', 'store_name',)

    def get_avg_rating(self):
        ratings = self.store_review.all()
        if ratings.exists():
            return round(sum([i.rating for i in ratings]) / ratings.count(), 1)
        return  0

    def get_total_people(self):
        people = self.store_review.all()
        if people.exists():
            if people.count() > 3:
                return '+3'
            return people.count()
        return 0

    def get_total_good(self):
        total = self.store_review.count()
        good = self.store_review.filter(rating__gt=3).count()
        return f'{round((good * 100) / total)}%' if total > 0 else '0%'


class StoreImage(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_images')
    store_image =models.ImageField(upload_to='store_image/')


class Contact_Info(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='contact_info')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    contact = PhoneNumberField(region='KG', null=True, blank=True)

    def __str__(self):
        return f'{self.user}'


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product', verbose_name='category')

    def __str__(self):
        return f"{self.product}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    product_image =models.ImageField(upload_to='product_image/')


class ComboProduct(models.Model):
    combo_name = models.CharField(max_length=32)
    combo_image = models.ImageField(upload_to='combo_images/', null=True, blank=True)
    combo_price =  models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='combo_product')
    description = models.TextField()

    def __str__(self):
        return f'{self.combo_name}, {self.store}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')
    creared_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.cart}, {self.quantity}, {self.product}'


class Order(models.Model):
    STATUS_CHOICES = (
        ('in delivery process', 'in delivery process'),
        ('awaiting processing', 'awaiting processing'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled')
    )
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_order')
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='in processing')
    delivery_address = models.CharField(max_length=40)
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_order')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.courier}, {self.products}, {self.delivery_address}'


class Courier(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='couriers')
    current_orders = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user}, {self.current_orders}'

    def get_avg_rating(self):
        ratings = self.store_review.all()
        if ratings.exists():
            return round(sum([i.rating for i in ratings]) / ratings.count(), 1)
        return  0

    def get_total_people(self):
        people = self.store_review.all()
        if people.exists():
            if people.count() > 3:
                return '+3'
            return people.count()
        return 0

    def get_total_good(self):
        total = self.store_review.count()
        good = self.store_review.filter(rating__gt=3).count()
        return f'{round((good * 100) / total)}%' if total > 0 else '0%'


class StoreReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_review')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.client} - {self.rating} - {self.store}'


class CourierReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    courier = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='courier_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.courier} - {self.rating}'


class Chat(models.Model):
    persom = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


