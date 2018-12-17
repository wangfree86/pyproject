from learn.sendmail.chapter7.crawl_info import get_info
from learn.sendmail.chapter7.send_mail import send_mail
if __name__ == '__main__':
    crawl_url = "https://tieba.baidu.com/p/2256306796?pn=1"
    content = get_info(crawl_url)
    # print(content)
    send_mail(content)

