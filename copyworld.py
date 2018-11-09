'''
操作剪切板：读取剪切板的字符串;清空剪切板;向剪切板中写入字符串（只能写入 ascii 字符）。
win10, python3, 
'''
from ctypes import *


user32 = windll.user32
kernel32 = windll.kernel32
def get_clipboard():
    user32.OpenClipboard(c_int(0))
    contents = c_char_p(user32.GetClipboardData(c_int(1))).value
    user32.CloseClipboard()
    return contents
def empty_clipboard():
    user32.OpenClipboard(c_int(0))
    user32.EmptyClipboard()
    user32.CloseClipboard()

def set_clipboard(data):
    user32.OpenClipboard(c_int(0))
    user32.EmptyClipboard()
    alloc = kernel32.GlobalAlloc(0x2000, len(bytes(data, encoding='utf_8'))+1)
    # alloc = kernel32.GlobalAlloc(0x2000, len(data)+1)
    lock = kernel32.GlobalLock(alloc)
    cdll.msvcrt.strcpy(c_char_p(lock),bytes(data, encoding='utf_8'))
    # cdll.msvcrt.strcpy(c_char_p(lock), data)
    kernel32.GlobalUnlock(alloc)
    user32.SetClipboardData(c_int(1),alloc)
    user32.CloseClipboard()
# if __name__ == '__main__':
#     # 获取剪切板内字符串
#     text_raw = get_clipboard()
#     # print('{0} {1}'.format(text_raw, type(text_raw)))
#
#     try:
#         text_str = text_raw.decode('utf_8')
#         print(text_str)
#         # print('{0} {1}'.format(text_str, type(text_str)))
#     except:
#         print('剪切板为空。')
if __name__ == '__main__':
    # 向剪切板内写入 ascii 字符串
    set_clipboard('ascii 字符串!')
    text = get_clipboard()
    print(text)