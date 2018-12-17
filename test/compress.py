#coding=utf-8
#!/usr/bin/env python
import Image
import os
import os.path
import sys
path = sys.argv[1]
small_path = (path[:-1] if path[-1]=='/' else path) +'_small'
if not os.path.exists(small_path):
    os.mkdir(small_path)
for root, dirs, files in os.walk(path):
    for f in files:
        fp = os.path.join(root, f)
        img = Image.open(fp)
        w, h = img.size
        img.resize((w/2, h/2)).save(os.path.join(small_path, f), "JPEG")
