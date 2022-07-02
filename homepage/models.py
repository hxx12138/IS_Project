from django.db import models
import datetime

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate

class cangku(models.Model):
    cangku_id = models.CharField(max_length=20, primary_key=True)
    cangku_dizhi = models.CharField(max_length=20)
    cangku_rongliang = models.FloatField(max_length=2)
    cangku_shengyu = models.FloatField(max_length=2)
    longitu = models.CharField(max_length=20, null=True)
    latitude = models.CharField(max_length=20, null=True)
    cangku_manager = models.CharField(max_length=20, null=True)

class gongyingshang(models.Model):
    gongyingshang_id = models.CharField(max_length=20, primary_key=True)
    gongyingshang_mingcheng = models.CharField(max_length=20, null=True)
    gongyingshang_dizhi = models.CharField(max_length=20, null=True)
    gongyingshang_dianhua = models.CharField(max_length=20, null=True)
    gongyingshang_jingdu = models.FloatField(max_length=20, null=True)
    gongyingshang_weidu = models.FloatField(max_length=20, null=True)

class yuancailiao(models.Model):
    yuancailiao_id = models.CharField(max_length=20, primary_key=True)
    yuancailiao_mingcheng = models.CharField(max_length=20, null=True)
    cangku_id = models.CharField(max_length=20, null=True, blank=True)
    gongyingshang_id = models.CharField(max_length=20, null=True, blank=True)
    yuancailiao_zhonglei = models.CharField(max_length=20, null=True, blank=True)
    yuancailiao_zhiliang = models.CharField(max_length=20, null=True, blank=True)
    yuancailiao_danjia = models.CharField(max_length=20, null=True, blank=True)
    shengchanriqi = models.DateField(null=True, blank=True)
    baozhiqi = models.CharField(max_length=20, null=True, blank=True)
    chandi = models.CharField(max_length=20, null=True, blank=True)
    gongyingshang_name = models.CharField(max_length=20, null=True, blank=True)
    yuancailiao_max = models.IntegerField(max_length=20, null=True, blank=True)

class yuangong(models.Model):
    yuangong_id = models.CharField(max_length=20, primary_key=True)
    bumen_id = models.CharField(max_length=20, null=True)
    bumen_mingcheng = models.CharField(max_length=20, null=True)
    yuangong_xingming = models.CharField(max_length=20, null=True)
    yuangong_xingbie = models.CharField(max_length=10, null=True)
    yuangong_dianhua = models.CharField(max_length=20, null=True)
    yuangong_nianling = models.IntegerField(max_length=20, null=True)
    shenfenzhenghao = models.CharField(max_length=20, null=True)
    yuangong_zhiwei = models.CharField(max_length=10, null=True)
    yuangong_zhuangtai = models.IntegerField(max_length=20, null=True)
    yuangong_xinchou = models.FloatField(max_length=10, null=True)

class shangpin(models.Model):
    shangpin_id = models.CharField(max_length=20, primary_key=True)
    cangku_id = models.CharField(max_length=20, null=True)
    shangpin_zhonglei = models.CharField(max_length=20, null=True)
    shangpin_zhiliang = models.CharField(max_length=20, null=True)
    shangpin_danjia = models.FloatField(max_length=10, null=True)
    shangpin_shengchanriqi = models.DateField(null=True)
    shangpin_baozhiqi = models.IntegerField(max_length=10, null=True)
    shangpin_chandi = models.CharField(max_length=20, null=True)
    rukushijian = models.DateField(null=True)
    shangpin_zhuangtai = models.CharField(max_length=20, null=True)
    shuliang = models.FloatField(max_length=20, null=True)  # 剩余数量
    suoshudingdan_id = models.CharField(max_length=20, null=True)
    yuancailiao_id=models.CharField(max_length=20, null=True)
    suoshugongyingshang_id = models.CharField(max_length=20, null=True)
    shanpin_chandi_longitude = models.FloatField(max_length=20, null=True)
    shanpin_chandi_latitude = models.FloatField(max_length=20, null=True)

class shouru(models.Model):
    shouru_id = models.CharField(max_length=20, primary_key=True)
    xiaoshou_id = models.CharField(max_length=20)
    shouru_shijian = models.DateField()
    zongjine = models.FloatField(max_length=20, null=True)  # 新增列
    type = models.CharField(max_length=20, null=True)  # 新增列

class zhichu(models.Model):
    zhichu_id = models.CharField(max_length=20, primary_key=True)
    caigou_id = models.CharField(max_length=20)
    gongyingshang_id = models.CharField(max_length=20)
    zhichu_shijian = models.DateField()
    zongjine = models.FloatField(max_length=20)
    type = models.CharField(max_length=20)

class bumen(models.Model):
    bumen_id = models.CharField(max_length=20, primary_key=True)
    bumen_mingcheng = models.CharField(max_length=20)

class caigoudingdan(models.Model):
    caigou_id = models.CharField(max_length=20, primary_key=True)
    gongyingshang_id = models.CharField(max_length=20, null=True)
    caigou_zongjine = models.CharField(max_length=20, null=True)
    yuqidaohuoshijian = models.DateField(null=True)
    huopinshuliang = models.FloatField(max_length=10, null=True)
    huopinzongjia = models.FloatField(max_length=10, null=True)
    caigoushijian = models.DateField(null=True)
    fuzeren = models.CharField(max_length=20, null=True)
    dingdanzhuangtai = models.CharField(max_length=20, null=True)
    pingzheng = models.CharField(max_length=20, null=True)
    yuancailiao_id = models.CharField(max_length=20, null=True)
    yuancailiao_shuliang = models.CharField(max_length=20, null=True)
    dingdanxiangqing = models.CharField(max_length=100, null=True)

class xiaoshoudingdan(models.Model):
    xiaoshou_id = models.CharField(max_length=20, primary_key=True)
    shourujilu_id = models.CharField(max_length=20, null=True)
    xiadanshijian = models.DateTimeField()
    xiaoshou_zongjine = models.FloatField(max_length=10, null=True)
    shouhuorenxingming = models.CharField(max_length=20, null=True)
    shouhuorenlianxi = models.CharField(max_length=20, null=True)
    shouhuodizhi = models.CharField(max_length=100, null=True)
    dingdanbeizhu = models.CharField(max_length=50, null=True)
    shangpin_goumaishuliang = models.IntegerField(max_length=10, null=True)
    shangpin_zongjia = models.FloatField(max_length=10, null=True)
    peisongweizhi = models.CharField(max_length=100, null=True)
    songdashijian = models.DateTimeField(null=True)
    peisongyuan_id = models.CharField(max_length=20, null=True)
    cangku_id = models.CharField(max_length=20, null=True, blank=True)
    dingdanzhuangtai = models.CharField(max_length=10, null=True, blank=True)
    dingdanzhuangtai = models.CharField(max_length=20, null=True)
    xiadanzhanghu = models.CharField(max_length=20, null=True)
    pingzhengbianhao = models.CharField(max_length=20, null=True)
    dingdanxiangqing = models.CharField(max_length=100, null=True)
    mudidi_jingdu = models.FloatField(max_length=10, null=True, blank=True)
    mudidi_weidu = models.FloatField(max_length=10, null=True, blank=True)
    cangku_jingdu = models.FloatField(max_length=10, null=True, blank=True)
    cangku_weidu = models.FloatField(max_length=10, null=True, blank=True)

#存储用户评价信息的数据表
class Rewards(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_content = models.CharField(max_length=2000)
    user_score = models.FloatField(max_length=2)
    user_time = models.DateField()

class Meta:
    unique_together = ('caigou_id', 'yuancailiao_id')