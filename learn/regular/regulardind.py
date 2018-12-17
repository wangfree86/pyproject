
import re
# 正则获取部分信息的办法
# .*任何字符串不限数量
# cat结尾的包含cta前面全部字符串
print(re.findall(r".*cat$", "dog runs to cat"))
# 任何字符串开头但是最后只能是runs
print(re.findall(r"^.*runs", "dog runs to cat"))

# 在（）区间中的任何字符串（）特殊字符加\
print(re.findall(r"\(.*\)", 'sdsfds+({eretr})+ljksdfds'))
# 在{}区间中的任何字符串
print(re.findall(r"{.*}", 'sdsfds+({eretr})+ljksdfds'))