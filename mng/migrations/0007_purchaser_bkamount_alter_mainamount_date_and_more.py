# Generated by Django 4.2 on 2023-05-24 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng', '0006_purchaser_w_amount_alter_mainamount_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaser',
            name='bkamount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainamount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 15, 36, 3, 386027)),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 15, 36, 3, 387027)),
        ),
    ]
