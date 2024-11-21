# Generated by Django 4.2.16 on 2024-11-20 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0002_cartitem_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="added_at",
        ),
        migrations.AddField(
            model_name="cart",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
