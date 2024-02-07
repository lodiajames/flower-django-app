# Generated by Django 4.2.6 on 2024-02-06 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="flower",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="myapp.category",
            ),
        ),
    ]