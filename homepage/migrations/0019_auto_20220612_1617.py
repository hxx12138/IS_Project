# Generated by Django 3.2.5 on 2022-06-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_shangpin_yuancailiao_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shangpin',
            name='cangku_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shangpin',
            name='rukushijian',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='shangpin',
            name='shangpin_baozhiqi',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='shangpin',
            name='shangpin_chandi',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shangpin',
            name='shangpin_danjia',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='shangpin',
            name='shangpin_shengchanriqi',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='shangpin',
            name='shangpin_zhiliang',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shangpin',
            name='shangpin_zhuangtai',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
