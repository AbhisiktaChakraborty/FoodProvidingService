# Generated by Django 3.2.4 on 2021-07-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raisemodifyorder', '0008_auto_20210708_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='person_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='address',
            name='person_role',
            field=models.CharField(default='', max_length=50),
        ),
    ]
