# Generated by Django 2.0.4 on 2018-04-30 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamples', '0004_auto_20180430_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tample',
            name='created_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
