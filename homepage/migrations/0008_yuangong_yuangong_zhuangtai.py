# Generated by Django 3.2.5 on 2022-06-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20220611_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='yuangong',
            name='yuangong_zhuangtai',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
