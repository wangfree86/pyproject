import requests
import re
import csv
import time

# https://gitbook.cn/books/5b88922e488ba027c5fac1c8/index.html

# 保存文件到cvs的例子
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
params = {
    'offset': 0
}


def get_html(page):
    # return None
    '''
    # 获取一页html页面
    # :param page: 页数
    # :return: 该页html页面
    # '''
    params['offset'] = page * 10
    url = 'http://maoyan.com/board/4'
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            html = response.text
            return html
        else:
            return -1
    except:
        return None


def parse_infor(html):
    '''
    提取html页面中的电影信息
    :param html: html页面
    :return: 电影信息列表
    '''
    pat = re.compile(
        '<div class="movie-item-info">.*?<p.*?><a.*?>(.*?)</a></p>.*?<p.*?>(.*?)</p>.*?<p.*?>(.*?)</p>.*?</div>.*?<div.*?>.*?<p.*?><i.*?>(.*?)</i><i.*?>(.*?)</i></p>.*?</div>.*?</div>.*?</div>',
        re.S)
    results = re.findall(pat, html)
    one_page_film = []
    if results:
        for result in results:
            film_dict = {}
            # 获取电影名信息
            film_dict['name'] = result[0]
            # 获取主演信息
            start = result[1]
            # 替换字符串中的 '\n' 字符，即换行字符
            start.replace('\n', '')
            # 去掉字符串两边的空格，并使用切片去除字符串开头的'主演：'三个字符
            start = start.strip()[3:]
            film_dict['start'] = start
            # 获取上映时间信息
            releasetime = result[2]
            # 使用切片去除字符串开头的'上映时间：'五个字符
            releasetime = releasetime[5:]
            film_dict['releasetime'] = releasetime
            # 获取评分信息
            left_half = result[3]
            right_half = result[4]
            score = left_half + right_half
            film_dict['score'] = score
            # 打印该电影信息：
            print(film_dict)
            # 将该电影信息字典存入一页电影列表中
            one_page_film.append(film_dict)
        return one_page_film
    else:
        return None


def save_infor(one_page_film):
    '''
    存储提取好的电影信息
    :param one_page_film: 电影信息列表
    :return: None
    '''
    with open('top_film.csv', 'a', newline='', errors='ignore') as f:
        csv_file = csv.writer(f)
        for one in one_page_film:
            csv_file.writerow([one['name'], one['start'], one['releasetime'], one['score']])


if __name__ == "__main__":
    # 利用循环构建页码
    for page in range(10):
        # 请求页面
        html = get_html(page)
        if html:
            # 提取信息
            one_page_film = parse_infor(html)
            if one_page_film:
                # 存储信息
                save_infor(one_page_film)
        else:
            print("hahha")
        time.sleep(1)
