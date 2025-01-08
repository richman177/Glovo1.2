# Generated by Django 5.1.4 on 2025-01-07 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_info',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_name',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='online_shop.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comboproduct',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='combo_products', to='online_shop.store'),
        ),
        migrations.AlterField(
            model_name='contact_info',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_contact', to='online_shop.store'),
        ),
        migrations.AlterField(
            model_name='product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='online_shop.store'),
        ),
    ]
