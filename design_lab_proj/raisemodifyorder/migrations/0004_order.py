# Generated by Django 3.2.4 on 2021-06-25 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raisemodifyorder', '0003_rename_adress_addresses_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('veg_healthy', models.IntegerField()),
                ('veg_ill', models.IntegerField()),
                ('nonveg_healthy', models.IntegerField()),
                ('nonveg_ill', models.IntegerField()),
                ('allergies', models.CharField(max_length=200)),
                ('delivery_address', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('food_seeker_id', models.IntegerField()),
                ('food_provider_id', models.IntegerField()),
            ],
        ),
    ]