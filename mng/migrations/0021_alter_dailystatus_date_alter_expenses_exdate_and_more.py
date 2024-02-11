# Generated by Django 4.2 on 2023-06-11 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng', '0020_alter_dailystatus_date_alter_expenses_exdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystatus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 14, 23, 32, 974815)),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='exdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 14, 23, 32, 973898)),
        ),
        migrations.AlterField(
            model_name='mainamount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 14, 23, 32, 969970)),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 14, 23, 32, 970828)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 14, 23, 32, 972827)),
        ),
        migrations.AlterField(
            model_name='salesdt',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 14, 23, 32, 976814)),
        ),
    ]