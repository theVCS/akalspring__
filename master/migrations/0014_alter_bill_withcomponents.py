# Generated by Django 4.0.4 on 2022-05-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0013_bill_descri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='withComponents',
            field=models.TextField(blank=True, default='(With Components)', null=True),
        ),
    ]
