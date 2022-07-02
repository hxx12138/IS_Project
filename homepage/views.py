from django.shortcuts import render,redirect
from homepage import models
from django.http import HttpResponse
from homepage.models import *
from homepage.models import xiaoshoudingdan, caigoudingdan, shangpin, Rewards, yuangong, yuancailiao
from homepage.utils.pagination import Pagination
import json
# Create your views here.


# hxx
# 首页
def home(req):
    return redirect('/login')

# 主页
def index(req):
    return render(req, 'index.html')

# 个人信息
def user_profile(req):
    return render(req, 'user-profile.html')

def login(req):
    return render(req, 'authentication-signin.html')


def error(req):
    return render(req, 'errors-404-error.html')


def department_management(req):
    return render(req, 'table-datatable-department.html')

def employee_management(req):
    data_list = yuangong.objects.all()
    print(data_list)

    return render(req, 'table-datatable-employee.html', {'data_list': data_list})

def sales_management(req):        #销售订单界面
    if req.method == 'GET':
        data_list = xiaoshoudingdan.objects.all().order_by('xiaoshou_id')
        page_object = Pagination(req, data_list)
        context = {
            "data_list": page_object.page_data_list,
            "page_string": page_object.html()
        }
        return render(req, 'sales_orders_management.html',context)
    sales_order_id = req.POST.get("soid")
    print(sales_order_id)
    info_tobe_found = xiaoshoudingdan.objects.filter(xiaoshou_id=sales_order_id).first()
    print(info_tobe_found.xiaoshou_id)
    return render(req, 'sales_order_search_result_management.html', {"data": info_tobe_found})

def add_sales_order_management(req):  #添加销售记录
    if req.method == 'GET':
        return render(req, 'add_sales_order_management.html')
    #获取用户提交的数据
    purchase_order_id = req.POST.get("id")
    zongjia = req.POST.get("sum")
    purchasedetails = req.POST.get("detail")
    dingdanbeizhu = req.POST.get("beizhu")
    fujian = req.POST.get("image-uploadify")
    name = req.POST.get("name")
    phone = req.POST.get("phone")
    time = req.POST.get("time")
    customer_id = req.POST.get("cid")
    dizhi = req.POST.get("dizhi")
    status = req.POST.get("status")
    pingzheng = req.POST.get("sid")
    xiaoshoudingdan.objects.create(xiaoshou_id=purchase_order_id, xiadanshijian=time, xiaoshou_zongjine=zongjia, dingdanxiangqing=purchasedetails,
                                    dingdanbeizhu=dingdanbeizhu, shouhuorenxingming=name, shouhuorenlianxi=phone, xiadanzhanghu = customer_id,
                                    dingdanzhuangtai=status, pingzhengbianhao = pingzheng, shouhuodizhi=dizhi)
    return redirect("/sales_orders_management")

def edit_sales_order_management(req): #编辑销售订单
    poid = req.GET.get('nid')
    if req.method == 'GET':
        # 修改信息
        info_tobe_edited = xiaoshoudingdan.objects.filter(xiaoshou_id=poid).first()
        return render(req, "edit_sales_order_management.html", {'info': info_tobe_edited})
        # return render(req, "friends_edit.html")
    purchase_order_id = req.POST.get("inputsalesorder")
    purchasedetails = req.POST.get("inputorderdescription")
    fujian = req.POST.get("image-uploadify")
    name = req.POST.get("inputcustomername")
    phone = req.POST.get("inputcustomerphone")
    time = req.POST.get("inputsalestime")
    customer_id = req.POST.get("inputcustomerid")
    wuliu_id = req.POST.get("inputwuliuid")
    status = req.POST.get("inputstatus")
    pingzheng = req.POST.get("inputsalesdocumentid")
    xiaoshoudingdan.objects.filter(xiaoshou_id=purchase_order_id).update(xiadanshijian=time, xiaoshou_zongjine=purchasedetails,
                                   shouhuorenxingming=name, shouhuorenlianxi=phone, peisongyuan_id=wuliu_id,
                                   xiadanzhanghu=customer_id,
                                   dingdanzhuangtai=status, pingzhengbianhao=pingzheng)
    return redirect("/sales_orders_management")

def delete_sales_order_management(req): #删除销售订单
    poid = req.GET.get('nid')
    xiaoshoudingdan.objects.filter(xiaoshou_id=poid).delete()
    return redirect("/sales_orders_management")

# wh

def wuliu(req):
    if req.method == 'GET':
        data_list=xiaoshoudingdan.objects.all().order_by('xiaoshou_id')
        return render(req,'wuliu.html',{"data_list":data_list})
    info=req.POST.get("cgid")
    if info[0:2]=='SO':
        info_tobe_found = xiaoshoudingdan.objects.filter(xiaoshou_id=info)
    elif info[0:2]=='WH':
        info_tobe_found = xiaoshoudingdan.objects.filter(cangku_id=info)
    elif info[0:2]=='CA':
        info_tobe_found = xiaoshoudingdan.objects.filter(xiadanzhanghu=info)
    elif info[0:2]=='PS':
        info_tobe_found = xiaoshoudingdan.objects.filter(peisongyuan_id=info)
    elif info in ['已送达','配送中','未配送']:
        info_tobe_found = xiaoshoudingdan.objects.filter(dingdanzhuangtai=info)
    #返回一个订单详情界面
    return render(req, 'wuliu.html', {"data_list": info_tobe_found})


def wuliu_time(req):
    id = req.GET.get("id")
    info_tobe_found = xiaoshoudingdan.objects.filter(xiaoshou_id=id)
    return render(req,'wuliu-time.html',{"data": info_tobe_found[0]})

def wuliu_mapp(req):
    id = req.GET.get("id")
    info_tobe_found = xiaoshoudingdan.objects.filter(xiaoshou_id=id)
    return render(req,'wuliu-map.html',{"data": info_tobe_found[0]})



'''def orm(req):
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs001',shourujilu_id='sr002',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小李',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps001',cangku_id='ck001',dingdanzhuangtai='已送达')
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs002',shourujilu_id='sr002',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小李',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps002',cangku_id='ck001',dingdanzhuangtai='配送中')
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs003',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='',cangku_id='ck001',dingdanzhuangtai='未配送')
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs004',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps003',cangku_id='ck002',dingdanzhuangtai='已送达')
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs005',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps001',cangku_id='ck003',dingdanzhuangtai='配送中')
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs006',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps004',cangku_id='ck002',dingdanzhuangtai='配送中')
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs007',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='',cangku_id='ck001',dingdanzhuangtai='未配送')
    #models.xiaoshoudingdan.objects.filter(xiaoshou_id='xs001').delete()
    return HttpResponse('成功')'''

'''def orm(req):
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs001',shourujilu_id='sr002',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小李',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps001',cangku_id='ck001',dingdanzhuangtai='已送达',mudidi_jingdu=116.38169,mudidi_weidu=40.003419,cangku_jingdu=116.310791,cangku_weidu=40.003519)
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs002',shourujilu_id='sr002',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小李',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps002',cangku_id='ck001',dingdanzhuangtai='配送中',mudidi_jingdu=116.347313,mudidi_weidu=39.981771,cangku_jingdu=116.310791,cangku_weidu=40.003519)
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs003',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='',cangku_id='ck001',dingdanzhuangtai='未配送',mudidi_jingdu=116.347313,mudidi_weidu=39.981771)
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs004',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps003',cangku_id='ck002',dingdanzhuangtai='已送达',mudidi_jingdu=116.347313,mudidi_weidu=39.981771)
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs005',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps001',cangku_id='ck003',dingdanzhuangtai='配送中',mudidi_jingdu=116.347313,mudidi_weidu=39.981771)
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs006',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='ps004',cangku_id='ck002',dingdanzhuangtai='配送中',mudidi_jingdu=116.347313,mudidi_weidu=39.981771)
    models.xiaoshoudingdan.objects.create(xiaoshou_id='xs007',shourujilu_id='sr003',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=131.8,shouhuorenxingming='小王',shouhuorenlianxi='1234567890',shouhuodizhi='北京航空航天大学新东门',dingdanbeizhu='无',shangpin_goumaishuliang=5,shangpin_zongjia=131.8,peisongweizhi='酷秀',songdashijian='2022-06-03 19:58:00',peisongyuan_id='',cangku_id='ck001',dingdanzhuangtai='未配送',mudidi_jingdu=116.347313,mudidi_weidu=39.981771)
    return HttpResponse('成功')'''

def orm(req):
    #xiaoshoudingdan.objects.create(xiaoshou_id='SO000001',shourujilu_id='IR00001',xiadanshijian='2022-06-03 19:32:31',xiaoshou_zongjine=100.8,shouhuorenxingming='王昊',shouhuorenlianxi='15822153412',shouhuodizhi='北京市海淀区学院路37号北京航空航天大学家属区',dingdanbeizhu='是 谁 憋 疯 了',songdashijian='2022-06-03 19:58:00',peisongyuan_id='PS0001',cangku_id='WH0001',dingdanzhuangtai='已送达',xiadanzhanghu='CA000001',pingzhengbianhao='SD000001',dingdanxiangqing='M000001:2;M000002:1',mudidi_jingdu=116.38169,mudidi_weidu=40.003419,cangku_jingdu=116.36611,cangku_weidu=39.91231)
    xiaoshoudingdan.objects.create(xiaoshou_id='SO000002',shourujilu_id='IR00002',xiadanshijian='2022-06-03 20:32:01',xiaoshou_zongjine=51.2,shouhuorenxingming='许嘉璐',shouhuorenlianxi='13785467098',shouhuodizhi='北京市海淀区清华园1号清华大学紫荆公寓',dingdanbeizhu='',songdashijian='2022-06-03 20:58:00',peisongyuan_id='PS0002',cangku_id='WH0001',dingdanzhuangtai='配送中',xiadanzhanghu='CA000002',pingzhengbianhao='SD000002',dingdanxiangqing='M000003:10',mudidi_jingdu=116.387313,mudidi_weidu=39.981771,cangku_jingdu=116.36611,cangku_weidu=39.91231)
    #xiaoshoudingdan.objects.create(xiaoshou_id='SO000003',shourujilu_id='IR00003',xiadanshijian='2022-06-04 09:05:43',xiaoshou_zongjine=31.9,shouhuorenxingming='何熙',shouhuorenlianxi='13920010354',shouhuodizhi='北京市海淀区颐和园路5号北京大学南门',dingdanbeizhu='无',songdashijian='2022-06-04 10:12:00',peisongyuan_id='',cangku_id='WH0002',dingdanzhuangtai='未配送',xiadanzhanghu='CA000003',pingzhengbianhao='SD000003',dingdanxiangqing='M000004:5',mudidi_jingdu=116.347313,mudidi_weidu=39.981771,cangku_jingdu=116.304779,cangku_weidu=39.973221)
    #xiaoshoudingdan.objects.create(xiaoshou_id='SO000004',shourujilu_id='IR00004',xiadanshijian='2022-06-04 10:35:32',xiaoshou_zongjine=41.5,shouhuorenxingming='张文翔',shouhuorenlianxi='15822943216',shouhuodizhi='北京市朝阳区工人体育场北路13号院天堂超市(北京总店)',dingdanbeizhu='无',songdashijian='2022-06-04 11:31:00',peisongyuan_id='PS0003',cangku_id='WH0002',dingdanzhuangtai='已送达',xiadanzhanghu='CA000004',pingzhengbianhao='SD000004',dingdanxiangqing='M000005:1;M000006:8',mudidi_jingdu=116.347313,mudidi_weidu=39.981771,cangku_jingdu=116.304779,cangku_weidu=39.973221)
    #xiaoshoudingdan.objects.create(xiaoshou_id='SO000005',shourujilu_id='IR00005',xiadanshijian='2022-06-05 15:19:28',xiaoshou_zongjine=32.6,shouhuorenxingming='韩淇',shouhuorenlianxi='13352178049',shouhuodizhi='北京市海淀区农大南路1号院厦门正航软件科技有限公司北京分公司',dingdanbeizhu='无',songdashijian='2022-06-05 15:58:00',peisongyuan_id='PS0001',cangku_id='WH0003',dingdanzhuangtai='配送中',xiadanzhanghu='CA000005',pingzhengbianhao='SD000005',dingdanxiangqing='M000007:2',mudidi_jingdu=116.347313,mudidi_weidu=39.981771,cangku_jingdu=116.45626,cangku_weidu=39.94793)
    xiaoshoudingdan.objects.create(xiaoshou_id='SO000006',shourujilu_id='IR00006',xiadanshijian='2022-06-06 13:31:30',xiaoshou_zongjine=11.4,shouhuorenxingming='王舵',shouhuorenlianxi='15027890560',shouhuodizhi='北京市海淀区海淀北二街8号中关村SOHO大厦',dingdanbeizhu='无',songdashijian='2022-06-06 14:21:00',peisongyuan_id='PS0004',cangku_id='WH0002',dingdanzhuangtai='配送中',xiadanzhanghu='CA000006',pingzhengbianhao='SD000006',dingdanxiangqing='M000001:2;M000008:2',mudidi_jingdu=116.347313,mudidi_weidu=39.981771,cangku_jingdu=116.304779,cangku_weidu=39.973221)
    #xiaoshoudingdan.objects.create(xiaoshou_id='SO000007',shourujilu_id='IR00007',xiadanshijian='2022-06-07 16:12:17',xiaoshou_zongjine=152.1,shouhuorenxingming='李忠昆',shouhuorenlianxi='13722840356',shouhuodizhi='北京市海淀区中关村大街59号中国人民大学西门',dingdanbeizhu='无',songdashijian='2022-06-07 17:37:00',peisongyuan_id='',cangku_id='WH0001',dingdanzhuangtai='未配送',xiadanzhanghu='CA000007',pingzhengbianhao='SD000007',dingdanxiangqing='M000009:7',mudidi_jingdu=116.347313,mudidi_weidu=39.981771,cangku_jingdu=116.36611,cangku_weidu=39.91231)
    #xiaoshoudingdan.objects.filter(xiaoshou_id='SO000002').delete()
    #xiaoshoudingdan.objects.filter(xiaoshou_id='SO000006').delete()
    #xiaoshoudingdan.objects.filter(xiaoshou_id='SO001212').delete()
    return HttpResponse('成功')



# zwx

# 以下是销售部门的子系统主页界面
def purchase_department(req):
    list_dic = yuancailiao.objects.all()
    yuancailiao_id_list = req.POST.getlist('yuancailiao_id')
    yuancailiao_zhonglei_list = req.POST.getlist('yuancailiao_zhonglei')
    gongyingshang_name_list = req.POST.getlist('gongyingshang_name')
    conditions = [yuancailiao_id_list, yuancailiao_zhonglei_list, gongyingshang_name_list]
    # print(conditions)

    page_object = Pagination(req, list_dic)

    if req.method == 'GET':
        return render(req, 'purchase_department.html',
                      {"list_dic": list_dic,
                       "list_dic_search": list_dic,
                       "page_string": page_object.html(),
                       })

    if yuancailiao_id_list == [] and yuancailiao_zhonglei_list == [] and gongyingshang_name_list == []:
        return render(req, 'purchase_department.html',
                      {"list_dic": list_dic,
                       "list_dic_search": list_dic,
                       "page_string": page_object.html(),
                       })

    # 添加条件
    list_dic_search = []

    if yuancailiao_id_list:
        for yuancailiao_id in yuancailiao_id_list:
            list_dic_i = yuancailiao.objects.filter(yuancailiao_id=yuancailiao_id)
            if list_dic_i not in list_dic_search:
                list_dic_search.extend(list_dic_i)

    if yuancailiao_zhonglei_list:
        for yuancailiao_zhonglei in yuancailiao_zhonglei_list:
            list_dic_i = yuancailiao.objects.filter(yuancailiao_zhonglei=yuancailiao_zhonglei)
            if list_dic_i not in list_dic_search:
                list_dic_search.extend(list_dic_i)

    if gongyingshang_name_list:
        for gongyingshang_name in gongyingshang_name_list:
            list_dic_i = yuancailiao.objects.filter(gongyingshang_name=gongyingshang_name)
            if list_dic_i not in list_dic_search:
                list_dic_search.extend(list_dic_i)

    # list_dic_search = list(set(list_dic_search))

    def sort_result(x):
        # 用来合并查重排序上述列表的函数
        x1 = []
        x2 = {}  # 过渡字典
        for i in range(len(x)):
            x2[x[i].yuancailiao_id] = x[i]
        x1 = sorted(x2.items(), key=lambda v: v[0])
        x3 = []
        for i in x1:
            x3.append(i[1])
        return x3

    list_dic_search = sort_result(list_dic_search)
    if list_dic_search:
        return render(req, 'purchase_department.html',
                      {"list_dic_search": list_dic_search,
                       "list_dic": list_dic,
                       "page_string": page_object.html(),
                       })
'''
def purchase_department_show(req):
    """
    models.yuancailiao.objects.create(
        yuancailiao_id="YCL0000002",
        cangku_id="CK0001",
        gongyingshang_id="GYS00002",
        gongyingshang_name = "伊利",
        yuancailiao_zhonglei="伊利牛奶",
        yuancailiao_zhiliang="特级",
        yuancailiao_danjia="￥5",
        yuancailiao_max = 10000,
        shengchanriqi="2022-06-07",
        baozhiqi="7",
        chandi="呼伦贝尔大草原")
    """
    """"""
    list_dic = models.yuancailiao.objects.all()

    return render(req, 'purchase_department_show.html', {"list_dic": list_dic})
'''

def GYS_show(req):
    gongyingshang_id = req.GET.get("gongyingshang_id")
    info = gongyingshang.objects.filter(gongyingshang_id=gongyingshang_id).first()

    if req.method == "GET":
        return render(req, 'GYS_show.html', {"info": info})
    return render(req, 'GYS_show.html', {"info": info})


def GYS_add(req):
    if req.method == "GET":
        return render(req, 'GYS_add.html')

    # 获取用户提交的数据
    yuancailiao_id = req.POST.get("yuancailiao_id")
    cangku_id = req.POST.get("cangku_id")
    gongyingshang_id = req.POST.get("gongyingshang_id")
    yuancailiao_zhonglei = req.POST.get("yuancailiao_zhonglei")
    yuancailiao_zhiliang = req.POST.get("yuancailiao_zhiliang")
    yuancailiao_danjia = req.POST.get("yuancailiao_danjia")
    shengchanriqi = req.POST.get("shengchanriqi")
    baozhiqi = req.POST.get("baozhiqi")
    chandi = req.POST.get("chandi")
    gongyingshang_name = req.POST.get("gongyingshang_name")
    yuancailiao_max = req.POST.get("yuancailiao_max")

    if shengchanriqi == '':
        shengchanriqi = "1900-01-01"
    if yuancailiao_max == '':
        yuancailiao_max = 0

    # 添加到数据库
    yuancailiao.objects.create(
        yuancailiao_id=yuancailiao_id,
        cangku_id=cangku_id,
        gongyingshang_id=gongyingshang_id,
        yuancailiao_zhonglei=yuancailiao_zhonglei,
        yuancailiao_zhiliang=yuancailiao_zhiliang,
        yuancailiao_danjia=yuancailiao_danjia,
        shengchanriqi=shengchanriqi,
        baozhiqi=baozhiqi,
        chandi=chandi,
        yuancailiao_max=yuancailiao_max,
        gongyingshang_name=gongyingshang_name,
    )
    return redirect("/purchase_department")
def GYS_edit(req):
    yuancailiao_id = req.GET.get('yuancailiao_id')
    if req.method == 'GET':
        # 修改信息
        GYS_edited = yuancailiao.objects.filter(yuancailiao_id=yuancailiao_id).first()

        return render(req, "GYS_edit.html", {'GYS_edited': GYS_edited})

    # 获取用户提交的数据
    yuancailiao_id = req.POST.get("yuancailiao_id")
    cangku_id = req.POST.get("cangku_id")
    gongyingshang_id = req.POST.get("gongyingshang_id")
    yuancailiao_zhonglei = req.POST.get("yuancailiao_zhonglei")
    yuancailiao_zhiliang = req.POST.get("yuancailiao_zhiliang")
    yuancailiao_danjia = req.POST.get("yuancailiao_danjia")
    shengchanriqi = req.POST.get("shengchanriqi")
    baozhiqi = req.POST.get("baozhiqi")
    chandi = req.POST.get("chandi")
    gongyingshang_name = req.POST.get("gongyingshang_name")
    yuancailiao_max = req.POST.get("yuancailiao_max")

    if shengchanriqi == '':
        shengchanriqi = "1900-01-01"
    if yuancailiao_max == '':
        yuancailiao_max = 0

    yuancailiao.objects.filter(yuancailiao_id=yuancailiao_id).update(
        yuancailiao_id=yuancailiao_id,
        cangku_id=cangku_id,
        gongyingshang_id=gongyingshang_id,
        yuancailiao_zhonglei=yuancailiao_zhonglei,
        yuancailiao_zhiliang=yuancailiao_zhiliang,
        yuancailiao_danjia=yuancailiao_danjia,
        shengchanriqi=shengchanriqi,
        baozhiqi=baozhiqi,
        chandi=chandi,
        yuancailiao_max=yuancailiao_max,
        gongyingshang_name=gongyingshang_name,
    )
    return redirect("/purchase_department")
def GYS_delete(req):
    # 删除供应商
    yuancailiao_id = req.GET.get('yuancailiao_id')
    yuancailiao.objects.filter(yuancailiao_id=yuancailiao_id).delete()
    return redirect("/purchase_department")
def details_purchase(req):
    yuancailiao_id = req.GET.get('yuancailiao_id')
    # print(yuancailiao_id)
    number = int(req.GET.get('number'))
    flag = int(req.GET.get('flag'))
    if flag == 1:
        number += 1
    if flag == 2:
        number -= 1

    if req.method == 'GET':
        # 修改信息
        details_purchase = yuancailiao.objects.filter(yuancailiao_id=yuancailiao_id).first()

        return render(req, "details_purchase.html",
                      {'details_purchase': details_purchase, 'number': number, "flag": flag})


'''    # 获取用户提交的数据
    yuancailiao_id = req.POST.get("yuancailiao_id")

    models.caigou_caigoudingdan.objects.create(caigou_yuancailiao_id=yuancailiao_id,

    )
    return render(req, "details_purchase.html", {'number': number})'''


def purchase_orders_show(req):
    if req.method == 'GET':
        res = {}
        data_list = caigoudingdan.objects.filter(dingdanzhuangtai="0").all()
        for obj in data_list:
            caigou_id = obj.caigou_id
            gongyingshang_id = obj.gongyingshang_id
            yuancailiao = obj.yuancailiao_id
            shuliang = obj.yuancailiao_shuliang
            if gongyingshang_id in res:
                res[gongyingshang_id] += ";" + yuancailiao + ":" + shuliang
            else:
                res[gongyingshang_id] = yuancailiao + ":" + shuliang
            caigoudingdan.objects.filter(caigou_id=caigou_id).delete()

        gongyingshang = list(res.keys())
        for i in range(len(gongyingshang)):
            caigou_id = "PO10000" + str(i)
            gongyingshang_id = gongyingshang[i]
            caigouzongjine = "20000"
            caigoushijian = datetime.datetime.now().strftime("%Y-%m-%d")
            yuqidaohuoshijian = "2022-06-15"
            fuzeren = "19377192"
            dingdanzhuangtai = "5"
            caigoudingdan.objects.create(caigou_id=caigou_id, gongyingshang_id=gongyingshang_id,
                                                caigou_zongjine=caigouzongjine,
                                                caigoushijian=caigoushijian, fuzeren=fuzeren,
                                                dingdanzhuangtai=dingdanzhuangtai,
                                                yuqidaohuoshijian=yuqidaohuoshijian)

        data_list = caigoudingdan.objects.filter(dingdanzhuangtai="5").all()
        page_object = Pagination(req, data_list)
        context = {
            "data_list": page_object.page_data_list,
            "page_string": page_object.html()
        }
        return render(req, 'purchase_orders_show.html', context)

def purchase_orders_make(req):
    id = req.GET.get("id")
    caigoudingdan.objects.filter(caigou_id=id).update(dingdanzhuangtai="1")
    return redirect("/purchase_orders_show/")

def purchase_orders_add(req):
    number = req.GET.get('number')                   #原材料购买数量
    yuancailiao_id = req.GET.get("yuancailiao_id")   #原材料id
    caigou_id = "Yg"+yuancailiao_id                  #构造订单编号
    info = yuancailiao.objects.filter(yuancailiao_id=yuancailiao_id).first()
    gongyingshang_id = info.gongyingshang_id
    caigoudingdan.objects.create(
        caigou_id=caigou_id,
        yuancailiao_id=yuancailiao_id,
        yuancailiao_shuliang=number,
        gongyingshang_id=gongyingshang_id,
        dingdanzhuangtai="0",
    )

    yuancailiao_max = int(info.yuancailiao_max) - int(number)

    yuancailiao.objects.filter(yuancailiao_id=yuancailiao_id).update(
        yuancailiao_max=yuancailiao_max)

    return redirect("/purchase_department/")
def purchase_orders_delete(req):
    #采购订单
    id = req.GET.get('id')
    caigoudingdan.objects.filter(caigou_id=id).delete()
    return redirect("/purchase_orders_show/")


def purchase_orders_edit(req):
    poid = req.GET.get('nid')
    if req.method == 'GET':
        # 修改信息
        info_tobe_edited = caigou_caigoudingdan.objects.filter(caigou_caigou_id=poid).first()
        return render(req, "purchase_orders_edit.html", {'info': info_tobe_edited})
        # return render(req, "friends_edit.html")
    details = req.POST.get("inputdetails")
    files = req.POST.get("image-uploadify")
    time = req.POST.get("inputdate")
    expect_time = req.POST.get("inputexpecttime")
    person = req.POST.get("inputid")
    supplier = req.POST.get("inputsupplierid")
    status = req.POST.get("inputstatus")
    pingzheng = req.POST.get("inputpdid")
    print(pingzheng)
    caigou_caigoudingdan.objects.filter(caigou_caigou_id=poid).update(
        caigou_caigou_zongjine=details, caigou_caigoushijian=time,
        caigou_yuqidaohuoshijian=expect_time, caigou_gongyingshang_id=supplier,
        caigou_fuzeren=person, caigou_dingdanzhuangtai=status, caigou_pingzheng=pingzheng)
    return redirect("/purchase_orders_show")


# xjl
#采购订单
def purchase_orders(req):      #采购订单界面
    if req.method == 'GET':
        data_list = caigoudingdan.objects.all().order_by('caigou_id')  #需要自己写的地方
        page_object = Pagination(req, data_list)
        context = {
                "data_list": page_object.page_data_list,
                "page_string": page_object.html()
        }
        return render(req, 'purchase_orders.html', context)

    #POST请求处理
    purchase_order_id = req.POST.get("poid")
    info_tobe_found = caigoudingdan.objects.filter(caigou_id=purchase_order_id).first()
    #返回一个订单详情界面
    return render(req, 'purchase_order_search_result.html', {"data": info_tobe_found})
#销售订单
def sales_orders(req):        #销售订单界面
    if req.method == 'GET':
        data_list = xiaoshoudingdan.objects.all().order_by('xiaoshou_id')
        page_object = Pagination(req, data_list)
        context = {
            "data_list": page_object.page_data_list,
            "page_string": page_object.html()
        }
        return render(req, 'sales_orders.html',context)
    sales_order_id = req.POST.get("soid")
    print(sales_order_id)
    info_tobe_found = xiaoshoudingdan.objects.filter(xiaoshou_id=sales_order_id).first()
    print(info_tobe_found.xiaoshou_id)
    return render(req, 'sales_order_search_result.html', {"data": info_tobe_found})
#收入记录
def income_manage(req): #收入管理界面
    if req.method == "GET":
        # for i in range(200):
        #     shouru.objects.create(shouru_id=i, xiaoshou_id="000001", shouru_shijian="2022-06-01", zongjine="5000", type="销售收入")
        data_list = shouru.objects.all().order_by('shouru_shijian')
        page_object = Pagination(req, data_list, page_size=10)
        context = {
            "data_list": page_object.page_data_list,
            "page_string": page_object.html()
        }
        return render(req, 'income_manage.html', context)

    else:
        info = req.POST.get("info")
        res = shouru.objects.filter(shouru_id=info).first()

        return render(req, 'income_manage_research.html', {"info": res})


        # page_object = Pagination(req, data_list)
        # context = {
        #     "data_list": page_object.page_data_list,
        #     "page_string": page_object.html()
        # }
        return render(req, 'income_manage.html', {"data_list": data_list})
#支出记录
def expenditure_manage(req): #支出管理界面
    if req.method == "GET":
        # for i in range(200):
        #     zhichu.objects.create(zhichu_id=i, caigou_id="000002", gongyingshang_id="0001", zhichu_shijian="2022-06-01", zongjine="10000", type="采购订单")
        data_list = zhichu.objects.all().order_by('zhichu_shijian')
        page_object = Pagination(req, data_list, page_size=10)
        context = {
            "data_list": page_object.page_data_list,
            "page_string": page_object.html()
        }
        return render(req, 'expenditure_manage.html', context)
    else:
        info = req.POST.get("info")
        res = zhichu.objects.filter(zhichu_id=info).first()

        return render(req, 'expenditure_manage_research.html', {"info": res})
#增加采购订单
def add_purchase_order(req): #添加采购记录
    if req.method == 'GET':
        return render(req, 'add_purchase_order.html')
    purchase_order_id = req.POST.get("id")
    zongjine = req.POST.get("sum")
    details = req.POST.get("details")
    files = req.POST.get("image-uploadify")
    time = req.POST.get("date")
    expect_time = req.POST.get("expectdate")
    person = req.POST.get("inputid")
    supplier = req.POST.get("sid")
    status = req.POST.get("inputstatus")
    pingzheng= req.POST.get("inputpdid")
    caigoudingdan.objects.create(caigou_id=purchase_order_id, caigou_zongjine=zongjine, caigoushijian=time,
                                 yuqidaohuoshijian=expect_time, gongyingshang_id=supplier, fuzeren=person,
                                 dingdanzhuangtai=status, pingzheng=pingzheng, dingdanxiangqing=details)
    return redirect("/purchase_orders")
#增加销售订单
def add_sales_order(req):  #添加销售记录
    if req.method == 'GET':
        return render(req, 'add_sales_order.html')
    #获取用户提交的数据
    purchase_order_id = req.POST.get("id")
    zongjia = req.POST.get("sum")
    purchasedetails = req.POST.get("detail")
    dingdanbeizhu = req.POST.get("beizhu")
    fujian = req.POST.get("image-uploadify")
    name = req.POST.get("name")
    phone = req.POST.get("phone")
    time = req.POST.get("time")
    customer_id = req.POST.get("cid")
    dizhi = req.POST.get("dizhi")
    status = req.POST.get("status")
    pingzheng = req.POST.get("sid")
    xiaoshoudingdan.objects.create(xiaoshou_id=purchase_order_id, xiadanshijian=time, xiaoshou_zongjine=zongjia, dingdanxiangqing=purchasedetails,
                                    dingdanbeizhu=dingdanbeizhu, shouhuorenxingming=name, shouhuorenlianxi=phone, xiadanzhanghu = customer_id,
                                    dingdanzhuangtai=status, pingzhengbianhao = pingzheng, shouhuodizhi=dizhi)
    return redirect("/sales_orders")
#编辑采购订单
def edit_purchase_order(req): #编辑采购订单
    poid = req.GET.get('nid')
    if req.method == 'GET':
        # 修改信息
        info_tobe_edited = caigoudingdan.objects.filter(caigou_id=poid).first()
        return render(req, "edit_purchase_order.html", {'info': info_tobe_edited})
        # return render(req, "friends_edit.html")
    poid = req.POST.get("nid")
    zong = req.POST.get("sum")
    details = req.POST.get("details")
    files = req.POST.get("image-uploadify")
    time = req.POST.get("time")
    expect_time = req.POST.get("expecttime")
    person = req.POST.get("cid")
    supplier = req.POST.get("sid")
    status = req.POST.get("status")
    pingzheng = req.POST.get("pdid")

    caigoudingdan.objects.filter(caigou_id=poid).update(caigou_zongjine=zong, dingdanxiangqing=details, caigoushijian=time, yuqidaohuoshijian=expect_time, gongyingshang_id=supplier, fuzeren=person, dingdanzhuangtai=status, pingzheng=pingzheng)

    return redirect("/purchase_orders")
def edit_purchase_order2(req): #编辑采购订单
    poid = req.GET.get('nid')
    if req.method == 'GET':
        # 修改信息
        info_tobe_edited = caigoudingdan.objects.filter(caigou_id=poid).first()
        return render(req, "edit_purchase_order2.html", {'info': info_tobe_edited})
        # return render(req, "friends_edit.html")
    poid = req.POST.get("nid")
    zong = req.POST.get("sum")
    details = req.POST.get("details")
    files = req.POST.get("image-uploadify")
    time = req.POST.get("time")
    expect_time = req.POST.get("expecttime")
    person = req.POST.get("cid")
    supplier = req.POST.get("sid")
    status = req.POST.get("status")
    pingzheng = req.POST.get("pdid")
    caigoudingdan.objects.filter(caigou_id=poid).update(caigou_zongjine=zong, caigoushijian=time, yuqidaohuoshijian=expect_time, gongyingshang_id=supplier, fuzeren=person, dingdanzhuangtai=status, pingzheng=pingzheng)

    return redirect("/receipt_confirm")
#删除采购订单
def delete_purchase_order(req): #删除采购订单
    poid = req.GET.get('nid')
    caigoudingdan.objects.filter(caigou_id=poid).delete()
    return redirect("/purchase_orders")
#订单支付功能
def purchase_order_payoff(req):
    id = req.GET.get("nid")
    info = caigoudingdan.objects.filter(caigou_id=id).first()
    zhichu.objects.create(zhichu_id = id, caigou_id=id, gongyingshang_id=info.gongyingshang_id, zhichu_shijian=datetime.datetime.now().strftime('%Y-%m-%d'),
                          zongjine = info.caigou_zongjine, type="采购支出")
    caigoudingdan.objects.filter(caigou_id=id).update(dingdanzhuangtai="3")
    return redirect("http://www.icbc.com.cn/icbc/")
#采购订单详情
def purchase_order_detail(req):                         #新增功能1
    poid = req.GET.get("nid")
    info = caigoudingdan.objects.filter(caigou_id=poid).first()
    print(info.caigou_zongjine)
    details={}
    details['tax'] = 0.25*float(info.caigou_zongjine)
    details['total'] = 1.25*float(info.caigou_zongjine)
    data = info.dingdanxiangqing
    ls = data.split(";")
    flag = 0
    data_list=[]
    for item in ls:
        flag += 1
        ans = item.split(":")
        data_list.append([flag, ans[0], ans[1], float(ans[1])*1.5, 1.5*float(ans[1])*float(ans[1])])
    return render(req, "purchase_order_detail.html", {"info": info, "data_list": data_list, "details": details})
#销售订单
def edit_sales_order(req): #编辑销售订单
    poid = req.GET.get('nid')
    if req.method == 'GET':
        # 修改信息
        info_tobe_edited = xiaoshoudingdan.objects.filter(xiaoshou_id=poid).first()
        return render(req, "edit_sales_order.html", {'info': info_tobe_edited})
        # return render(req, "friends_edit.html")
    sales_order_id = req.POST.get("nid")
    details = req.POST.get("details")
    fujian = req.POST.get("image-uploadify")
    name = req.POST.get("name")
    phone = req.POST.get("phone")
    dizhi = req.POST.get("location")
    customer_id = req.POST.get("inputcustomerid")
    time = req.POST.get("time")
    wuliu_id = req.POST.get("inputwuliuid")
    status = req.POST.get("inputstatus")
    pingzheng = req.POST.get("inputsalesdocumentid")
    xiaoshoudingdan.objects.filter(xiaoshou_id=sales_order_id).update(xiadanshijian=time, dingdanxiangqing=details,
                                   shouhuorenxingming=name, shouhuorenlianxi=phone, peisongyuan_id=wuliu_id,
                                   xiadanzhanghu=customer_id, peisongweizhi=dizhi,
                                   dingdanzhuangtai=status, pingzhengbianhao=pingzheng)
    return redirect("/sales_orders")
#删除销售订单
def delete_sales_order(req): #删除销售订单
    poid = req.GET.get('nid')
    xiaoshoudingdan.objects.filter(xiaoshou_id=poid).delete()
    return redirect("/sales_orders")
#开具发票
def make_invoice(req):
    poid = req.GET.get('nid')
    info = xiaoshoudingdan.objects.filter(xiaoshou_id=poid).first()

    return render(req, "make_invoice.html", {"info": info})
#销售订单详情
def sales_order_detail(req):
    soid = req.GET.get("nid")
    info = xiaoshoudingdan.objects.filter(xiaoshou_id=soid).first()
    data = info.dingdanxiangqing
    ls = data.split(";")
    flag = 0
    data_list=[]
    for item in ls:
        flag += 1
        ans = item.split(":")
        data_list.append([flag, ans[0], ans[1]])
    print(data_list)
    return render(req, "sales_order_detail.html", {"info": info, "data_list": data_list})
#库存部门
#采购订单入库确认
def receipt_confirm(req):        #订单核验、到库
    if req.method == 'GET':
        data_list = caigoudingdan.objects.all().order_by('caigou_id')
        page_object = Pagination(req, data_list)
        context = {
            "data_list": page_object.page_data_list,
            "page_string": page_object.html()
        }
        return render(req, "receipt_confirm.html", context)
    id = req.POST.get("poid")
    info_tobe_found = caigoudingdan.objects.filter(caigou_id=id).first()
    return render(req, 'purchase_order_search_result2.html', {"data": info_tobe_found})
#确定单个采购订单入库
def purchase_order_confirm(req):
    id = req.GET.get("nid")
    info = caigoudingdan.objects.filter(caigou_id=id).first()
    details = info.dingdanxiangqing   #整个订单的全部详细内容
    ls = details.split(";")
    for item in ls:
        print(item)
        gid = item.split(":")[0]
        quan = item.split(":")[1]
        one = yuancailiao.objects.filter(yuancailiao_id=gid).first()
        '''shangpin.objects.create(shangpin_id=one.yuancailiao_id, cangku_id="0001", yuancailiao_id=gid, shangpin_shengchanriqi=one.shengchanriqi,
                                shangpin_baozhiqi=one.baozhiqi, shangpin_chandi=one.chandi, rukushijian="2022-06-13", shangpin_zhuangtai="阴性",
                                shuliang=quan, shangpin_zhonglei=one.yuancailiao_mingcheng, shangpin_zhiliang="特级")'''
    caigoudingdan.objects.filter(caigou_id=id).delete()
    return redirect("/receipt_confirm/")
#库存信息管理
def storage_details(req):
    if req.method == 'GET':
        # for i in range(200):
        #     shangpin.objects.create(shangpin_id=i, cangku_id="0001", yuancailiao_id=i, shangpin_zhonglei="苹果",
        #                             shangpin_zhiliang="特级", shangpin_danjia="5", shangpin_shengchanriqi="2022-06-01",
        #                             shangpin_baozhiqi="21", shangpin_chandi="山东省烟台市栖霞市胶东农场", rukushijian="2022-06-03",
        #                             shangpin_zhuangtai="阴性", shuliang="100")
        data_list = shangpin.objects.all().order_by('shangpin_id')
        page_object = Pagination(req, data_list)
        context = {
            "data_list": page_object.page_data_list,
            "page_string": page_object.html()
        }
        return render(req, "storage_details.html", context)
    else:
        info = req.POST.get("info")
        res = info.split()
        shuxing = res[0]
        value = res[1]
        if shuxing == "编号":
            infos = shangpin.objects.filter(shangpin_id=value).first()
            return render(req, "shangpin_search_result1.html", {"info": infos})
        elif shuxing == "商品名称":
            infos = shangpin.objects.filter(shangpin_zhonglei=value).all()
            return render(req, "shangpin_search_result2.html", {"infos": infos})
    #POST请求是一个模糊搜索策略
#修改库存信息
def edit_storage(req):
    id = req.GET.get("nid")
    if req.method == "GET":
        print(id)
        info = shangpin.objects.filter(shangpin_id=id).first()
        return render(req, "edit_storage.html", {"info": info})
    cangku_id = req.POST.get("cangku")
    shangpin_zhonglei = req.POST.get("name")
    shangpin_zhiliang = req.POST.get("zhiliang")
    shangpin_danjia = req.POST.get("price")
    shangpin_chandi = req.POST.get("chandi")
    shuliang = req.POST.get("shuliang")
    baozhiqi = req.POST.get("baozhiqi")
    status = req.POST.get("status")

    shangpin.objects.filter(shangpin_id= id).update(cangku_id=cangku_id, shangpin_zhonglei=shangpin_zhonglei, shangpin_zhiliang=shangpin_zhiliang,
                                                    shangpin_danjia=shangpin_danjia, shangpin_chandi=shangpin_chandi,
                                                    shuliang = shuliang, shangpin_baozhiqi = baozhiqi, shangpin_zhuangtai=status)
    return redirect("/storage_details/")
#仓库详情页面
def warehouse_manage(req):
    return render(req, "warehouse_manage.html")
#出库管理页面
def ex_warehouse(req):
    if req.method == "GET":
        data_list = xiaoshoudingdan.objects.filter(dingdanzhuangtai="未配送").order_by("xiaoshou_id")
        page_object = Pagination(req, data_list)
        context = {
            "data_list": page_object.page_data_list,
            "page_string": page_object.html()
        }
        return render(req, "ex_warehouse.html", context)
    else:
        id = req.POST.get("id")
        cangku = req.POST.get("cangku")
        info = xiaoshoudingdan.objects.filter(xiaoshou_id=id).first()
        details = info.dingdanxiangqing
        ls = details.split(";")
        goods = shangpin.objects.all().order_by("shangpin_id")
        flag = 1
        for item in ls:
            gid = item.split(":")[0]
            quan = item.split(":")[1]
            for good in goods:
                if gid == good.shangpin_id and good.cangku_id == cangku and good.shuliang >= quan:
                    res = good.shuliang - quan
                    shangpin.objects.fileter(shangpin_id=gid).update(shuliang=res)
                else:
                    flag = 0
        if flag == 1:
            xiaoshoudingdan.objects.filter(xiaoshou_id=id).update(dingdanzhuangtai="配送中")
            return redirect('/ex_warehouse/')
        else: #库存不足
            return render(req, "ex_raise_error.html")

'''def home(req):
    return render(req, "home.html")'''

#hq
# 评论信息的展示
def page_kf(request):
    users = Rewards.objects.order_by('-user_time')[:20]  # 获取我们的数据库信息
    # return render(request,'table.html',{'form':table_form})
    return render(request, "kefu_mainpage.html", {'users': users})  # 必须用这个return



def to_wuliu(request):
    student_id = request.GET.get("id")
    #sub = xiaoshoudingdan.objects.get(xiaoshou_id=student_id)
    #data = {"id": sub.id, "课程id": sub.cour_id, "课程": sub.course, "成绩": sub.grade}
    return render(request,"wuliu.html")


def suyuan_search(req):
    address_longitude = []
    address_latitude = []
    address_data = []
    xiaoshou_id = req.POST.get('xiaoshou_id_key')
    if not xiaoshou_id:
        xiaoshou_id=req.GET.get('id')
        suyuan_info = shangpin.objects.filter(suoshudingdan_id=xiaoshou_id)
        for i in suyuan_info:
            address_data.append(str(i.shangpin_chandi) + "\n" + "(" + str(i.shanpin_chandi_longitude) + "," + str(
                i.shanpin_chandi_latitude) + ")")
            address_longitude.append(i.shanpin_chandi_longitude)
            address_latitude.append(i.shanpin_chandi_latitude)
        return render(req, "dingdan_suyuan.html", {'suyuan_info': suyuan_info, 'xiaoshou_id': xiaoshou_id,
                                                'address_longitude': json.dumps(address_longitude),
                                                'address_latitude': json.dumps(address_latitude),
                                                'address_data': json.dumps(address_data)})
    else:
        suyuan_info = shangpin.objects.filter(suoshudingdan_id=xiaoshou_id)
        for i in suyuan_info:
            address_data.append(str(i.shangpin_chandi) + "\n" + "(" + str(i.shanpin_chandi_longitude) + "," + str(
                i.shanpin_chandi_latitude) + ")")
            address_longitude.append(i.shanpin_chandi_longitude)
            address_latitude.append(i.shanpin_chandi_latitude)
        return render(req, "dingdan_suyuan.html", {'suyuan_info': suyuan_info, 'xiaoshou_id': xiaoshou_id,
                                                'address_longitude': json.dumps(address_longitude),
                                                'address_latitude': json.dumps(address_latitude),
                                                'address_data': json.dumps(address_data)})



def suyuan_details(req):
    poid = req.GET.get('nid')
    shangpin_info = shangpin.objects.filter(shangpin_id=poid).first()
    xiaoshoudingdan_info = xiaoshoudingdan.objects.filter(xiaoshou_id=shangpin_info.suoshudingdan_id).first()
    gongyingshang_info = gongyingshang.objects.filter(gongyingshang_id=shangpin_info.suoshugongyingshang_id).first()
    cangku_info = cangku.objects.filter(cangku_id=shangpin_info.cangku_id).first()
    manager = yuangong.objects.filter(yuangong_id=cangku_info.cangku_manager).first()
    peisongyuan_info = yuangong.objects.filter(yuangong_id=xiaoshoudingdan_info.peisongyuan_id).first()
    return render(req, "suyuan_details.html", {'shangpin': shangpin_info, 'peisongyuan': peisongyuan_info,
                                               'gongyingshang': gongyingshang_info, 'cangku': cangku_info,
                                               'manager': manager, 'xiaoshoudingdan': xiaoshoudingdan_info})