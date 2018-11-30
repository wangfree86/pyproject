import pyperclip
# 复制
str='天气：晴    1-15°C\n' \
    '本月余额21天'
pyperclip.copy(str)

# 粘贴
spam = pyperclip.paste()
print(spam)