import requests
# https://gitbook.cn/books/5b88922e488ba027c5fac1c8/index.html
# 而当我们查看该网页源代码时，却并没有电影相关的票房等信息，那么可以判断该页面可能使用了 Ajax
# （即“Asynchronous Javascript And XML”（异步 JavaScript 和 XML））技术，即动态网页（是指跟静态
# 网页相对的一种网页编程技术。静态网页，随着html代码的生成，页面的内容和显示效果就基本上不会发生变化了—
# —除非你修改页面代码。而动态网页则不然，页面代码虽然没有变，但是显示的内容却是可以随着时间、环境或者数据
# 库操作的结果而发生改变）。我们可以利用浏览器的开发者工具进行分析：
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


def get_html():
    '''
    获取JSON文件
    :return: JSON格式的数据
    '''
    # 请求second.json的URL
    url = 'https://box.maoyan.com/promovie/api/box/second.json'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # 由于是JSON文件，我们可以返回JSON格式的数据便于后续提取
            return response.json()
        else:
            return -1
    except:
        return None


def parse_infor(json):
    '''
    从JSON数据中提取电影票房数据，包括：电影名，上映信息，综合票房，票房占比，累计票房
    :param json: JSON格式的数据
    :return: 每次循环返回一次字典类型的电影数据
    '''
    if json:
        # 利用json中的get()方法层层获取对应的信息
        items = json.get('data').get('list')
        for item in items:
            piaofang = {}
            piaofang['电影名'] = item.get('movieName')
            piaofang['上映信息'] = item.get('releaseInfo')
            piaofang['综合票房'] = item.get('boxInfo')
            piaofang['票房占比'] = item.get('boxRate')
            piaofang['累计票房'] = item.get('sumBoxInfo')
            # 利用生成器每次循环都返回一个数据
            yield piaofang
    else:
        return None


def save_infor(results):
    '''
    存储格式化的电影票房数据HTML文件
    :param results: 电影票房数据的生成器
    :return: None
    '''
    rows = ''
    for piaofang in results:
        # 利用Python中的format字符串填充html表格中的内容
        row = '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(piaofang['电影名'],
                                                                                        piaofang['上映信息'],
                                                                                        piaofang['综合票房'],
                                                                                        piaofang['票房占比'],
                                                                                        piaofang['累计票房'])
        # 利用字符串拼接循环存储每个格式化的电影票房信息
        rows = rows + '\n' + row
    # 利用字符串拼接处格式化的HTML页面
    piaofang_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>电影票房</title>

</head>
<body>
    <style>
    .table1_5 table {
        width:100%;
        margin:15px 0
    }
    .table1_5 th {
        background-color:#00BFFF;
        color:#FFFFFF
    }
    .table1_5,.table1_5 th,.table1_5 td
    {
        font-size:0.95em;
        text-align:center;
        padding:4px;
        border:1px solid #dddddd;
        border-collapse:collapse
    }
    .table1_5 tr:nth-child(odd){
        background-color:#aae9fe;
    }
    .table1_5 tr:nth-child(even){
        background-color:#fdfdfd;
    }
    </style>
    <table class='table1_5'>
    <tr>
    <th>电影名</th>
    <th>上映信息</th>
    <th>综合票房</th>
    <th>票房占比</th>
    <th>累计票房</th>
    </tr>
    ''' + rows + '''
    </table>
</body>
</html>
    '''
    # 存储已经格式化的html页面
    with open('piaofang.html', 'w', encoding='utf-8') as f:
        f.write(piaofang_html)


if __name__ == "__main__":
    # 获取信息
    json = get_html()
    # 提取信息
    results = parse_infor(json)
    # 存储信息
    save_infor(results)