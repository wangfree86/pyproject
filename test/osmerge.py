# 合并文件
# 从一个文件获取需要合并的全部ts文件名称，然后在去合并全部ts成为一个mp4文件
import os
#exec_str = r'copy /b  ts/c9645620628078.ts+ts/c9645620628079.ts  ts/1.ts'
#os.system(exec_str) 
f = open('9cccf4a2-cfd0-4c39-9073-c033b0d2b6c1_pc_high.m3u8', 'r', encoding='utf-8')
text_list = f.readlines()
files = []
for i in text_list:
    if i.find('#EX')==-1:
        files.append(i)

f.close()


tmp = []
for file in files[0:450]:
    tmp.append(file.replace("\n",""))
    # 合并ts文件
os.chdir("download/")
shell_str = '+'.join(tmp)
shell_str = 'copy /b '+ shell_str + ' 5.mp4'
print(shell_str)
os.system(shell_str)
print(shell_str)