# Generated by Django 3.2.5 on 2022-05-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bumen',
            fields=[
                ('bumen_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('bumen_mingcheng', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='caigoudingdan',
            fields=[
                ('caigou_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('gongyingshang_id', models.CharField(max_length=20)),
                ('caigou_zongjine', models.CharField(max_length=20)),
                ('yuqidaohuoshijian', models.DateField()),
                ('huopinshuliang', models.FloatField(max_length=10)),
                ('huopinzongjia', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='cangku',
            fields=[
                ('cangku_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cangku_dizhi', models.CharField(max_length=20)),
                ('cangku_rongliang', models.FloatField(max_length=2)),
                ('cangku_shengyu', models.FloatField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='gongyingshang',
            fields=[
                ('gongyingshang_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('gongyingshang_mingcheng', models.CharField(max_length=20)),
                ('gongyingshang_dizhi', models.CharField(max_length=20)),
                ('gongyingshang_dianhua', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='shangpin',
            fields=[
                ('shangpin_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cangku_id', models.CharField(max_length=20)),
                ('shangpin_zhonglei', models.CharField(max_length=20)),
                ('shangpin_zhiliang', models.CharField(max_length=20)),
                ('shangpin_danjia', models.FloatField(max_length=10)),
                ('shangpin_shengchanriqi', models.DateField()),
                ('shangpin_baozhiqi', models.IntegerField(max_length=10)),
                ('shangpin_chandi', models.CharField(max_length=20)),
                ('rukushijian', models.DateField()),
                ('shangpin_zhuangtai', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='shouru',
            fields=[
                ('shouru_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('xiaoshou_id', models.CharField(max_length=20)),
                ('shouru_shijain', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='xiaoshoudingdan',
            fields=[
                ('xiaoshou_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('shourujilu_id', models.CharField(max_length=20)),
                ('xiadanshijian', models.DateField()),
                ('xiaoshou_zongjine', models.FloatField(max_length=10)),
                ('shouhuorenxingming', models.CharField(max_length=20)),
                ('shouhuorenlianxi', models.CharField(max_length=20)),
                ('shouhuodizhi', models.CharField(max_length=20)),
                ('dingdanbeizhu', models.CharField(max_length=50)),
                ('shangpin_goumaishuliang', models.IntegerField(max_length=10)),
                ('shangpin_zongjia', models.FloatField(max_length=10)),
                ('peisongweizhi', models.CharField(max_length=20)),
                ('songdashijian', models.DateField()),
                ('peisongyuan_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='yuancailiao',
            fields=[
                ('yuancailiao_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cangku_id', models.CharField(max_length=20)),
                ('gongyingshang_id', models.CharField(max_length=20)),
                ('yuancailiao_zhonglei', models.CharField(max_length=20)),
                ('yuancailiao_zhiliang', models.CharField(max_length=20)),
                ('yuancailiao_danjia', models.CharField(max_length=20)),
                ('shengchanriqi', models.DateField()),
                ('baozhiqi', models.IntegerField(max_length=10)),
                ('chandi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='yuangong',
            fields=[
                ('yuangong_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('bumen_id', models.CharField(max_length=20)),
                ('yuangong_xingming', models.CharField(max_length=20)),
                ('yuangong_xingbie', models.CharField(max_length=10)),
                ('yuangong_dianhua', models.CharField(max_length=20)),
                ('shenfenzhenghao', models.CharField(max_length=20)),
                ('yuangong_zhiwei', models.CharField(max_length=10)),
                ('yuangong_xinchou', models.FloatField(max_length=10)),
            ],
        ),
    ]