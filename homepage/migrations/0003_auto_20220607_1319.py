# Generated by Django 3.2.5 on 2022-06-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20220607_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xiaoshoudingdan',
            name='songdashijian',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='xiaoshoudingdan',
            name='xiadanshijian',
            field=models.DateTimeField(),
        ),
    ]