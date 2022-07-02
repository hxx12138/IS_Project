"""

如果想要使用分页组件：
1、根据自己的情况筛选自己的数据
2、实例化分页对象，page_data_list:分完页的数据；page_string:生成页码
3、在html文件中table部分循环调用输出结果
在页面底端
<ul class="pagination">
{{ page_string }}
</ul>
生成页码
"""
from django.utils.safestring import mark_safe

class Pagination(object):
    def __init__(self, req, data_list, page_size=8, page_param="page", plus= 5):
        """
        :param req:请求的对象
        :param data_list: 符合条件的数据
        :param page_size: 每页要显示多少记录
        :param page_param: 在URL中传递的获取分页的参数，例如：http://127.0.0.1:8000/purchase_orders/?page=10
        :param plus: 显示前/后几页
        """
        page = req.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_data_list = data_list[self.start:self.end]

        total_count = data_list.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据比较少，都没有达到11页。
            start_page = 1
            end_page = self.total_page_count
        else:
            # 当前页<5时
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页 > 5
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        page_str_list = []

        # 首页
        page_str_list.append('<li class="page-item"><a class="page-link" href="?page=1">首页</a></li>')

        # 上一页
        if self.page > 1:
            prev = '<li class="page-item"><a class="page-link" href="?page={}">上一页</a></li>'.format(self.page - 1)
        else:
            prev = '<li class="page-item"><a class="page-link" href="?page={}">上一页</a></li>'.format(1)
        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            if i == self.page:
                ele = '<li class="page-item active"><a class="page-link" href="?page={}">{}</a></li>'.format(i, i)
            else:
                ele = '<li class="page-item"><a class="page-link" href="?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            prev = '<li class="page-item"><a class="page-link" href="?page={}">下一页</a></li>'.format(self.page + 1)
        else:
            prev = '<li class="page-item"><a class="page-link" href="?page={}">下一页</a></li>'.format(self.total_page_count)
        page_str_list.append(prev)

        # 尾页
        page_str_list.append(
            '<li class="page-item"><a class="page-link" href="?page={}">尾页</a></li>'.format(self.total_page_count))

        search_string = """
               <li>
                   <form style="float: left;margin-left: -1px" method="get">
                       <input name="page"
                           style="position: relative;float:left;display: inline-block;width: 88px;border-radius: 0;"
                           type="text" class="form-control" placeholder="页码">
                       <button style="border-radius: 0" class="btn btn-primary radius-30 mt-2 mt-lg-0" type="submit">跳转</button>
                   </form> 
               </li>
               """
        page_str_list.append(search_string)

        page_string = mark_safe("".join(page_str_list))
        return page_string
