# Generated by Django 3.2.10 on 2022-06-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0014_alter_bill_withcomponents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='discount',
            field=models.FloatField(default=0),
        ),
    ]
