# 导入 requests 模块
import requests
# 在Headers中添加User-Agent字段信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
# 发起Get请求
response = requests.get("https://www.zhihu.com", headers=headers)
# 状态码
print(response.status_code)
# 响应体内容
print(response.text)