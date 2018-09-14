from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
src='http://data.5sing.kgimg.com/G130/M08/03/09/IocBAFsnoXiAFOWgAJaOXJvj13Q573.mp3'
# src='https://upload.jianshu.io/users/upload_avatars/3921613/22db2960-84a8-4c0c-bdc4-3a2cee78cc95.png?imageMogr2/auto-orient/strip|imageView2/1/w/240/h/240'
import requests
r = requests.get(src)
with open('../img/111.mp3', 'wb') as f:
    f.write(r.content)