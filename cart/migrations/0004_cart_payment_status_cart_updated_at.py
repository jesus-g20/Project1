# Generated by Django 4.2.16 on 2024-12-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0003_remove_cartitem_added_at_cart_active_alter_cart_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("failed", "Failed"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
