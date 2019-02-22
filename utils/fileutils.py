import json


# 写json文件
def write_json(data, json_file):
    with open(json_file, "w") as f:
        j = json.dumps(data, ensure_ascii=False)
        f.write(j)
