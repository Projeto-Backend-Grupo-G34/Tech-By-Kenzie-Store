# Generated by Django 4.2.2 on 2023-06-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]