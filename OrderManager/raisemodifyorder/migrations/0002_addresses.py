# Generated by Django 3.2.4 on 2021-06-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raisemodifyorder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.IntegerField()),
                ('person_role', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=200)),
            ],
        ),
    ]
