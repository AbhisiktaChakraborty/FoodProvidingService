# Generated by Django 3.1.5 on 2021-07-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodServices', '0002_auto_20210708_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodprovider',
            name='ratings',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
