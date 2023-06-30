# Generated by Django 4.2.2 on 2023-06-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('carts', models.ManyToManyField(
                    related_name='product', to='carts.cart')),
                ('orders', models.ManyToManyField(
                    related_name='product', to='orders.order')),
            ],
        ),
    ]
