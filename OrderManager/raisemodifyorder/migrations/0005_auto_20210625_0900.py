# Generated by Django 3.2.4 on 2021-06-25 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raisemodifyorder', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='allergies',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='food_provider_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='nonveg_healthy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='nonveg_ill',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='veg_healthy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='veg_ill',
            field=models.IntegerField(null=True),
        ),
    ]
