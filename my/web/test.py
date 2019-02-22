import sys
import json
from TGetStock import *
import utils.cvsutils as cvs
import utils.fileutils as file
import constant

import csv
import json


# 写json文件
def write_json(data, json_file):
    with open(json_file, "w") as f:
        j = json.dumps(data, ensure_ascii=False)
        f.write(j)
        print(j)


print(cvs.read_csv_json(constant.savecsv + 'a股2倍多.csv'))
file.write_json(cvs.read_csv_json(constant.savecsv + 'a股2倍多.csv'), 'a1股2倍多.json')
