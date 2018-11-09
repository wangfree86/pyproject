# -*- coding: utf-8 -*- 
import xdrlib, sys
import xlrd
import xml.dom.minidom


# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
def savexml(managerList, name):
    doc = xml.dom.minidom.Document()
    # 创建一个根节点Managers对象
    root = doc.createElement('AREA')
    doc.appendChild(root)
    for i in managerList:
        nodeManager = doc.createElement('item')
        # 子节点添加属性
        nodeManager.setAttribute("code", i['PLACECODE'])
        nodeManager.setAttribute("desc", i['PLACENAME'])
        root.appendChild(nodeManager)
    # 开始写xml文档
    fp = open('C:\\Users\\XH\\Desktop\\省市更新2018年11月8日 星期四\\第三期地址\\' + name, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


# 打开excel文件
def open_excel(file='test.xlsx'):
    # try:
    data = xlrd.open_workbook(file)
    return data
    # except Exception,e:
    #     print str(e)


# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
def excel_table_byname(file='san.xlsx', colnameindex=0, by_name=u'san'):
    data = open_excel(file)  # 打开excel文件
    table = data.sheet_by_name(by_name)  # 根据sheet名字来获取excel中的sheet
    nrows = table.nrows  # 行数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []  # 装读取结果的序列
    for rownum in range(0, nrows):  # 遍历每一行的内容
        row = table.row_values(rownum)  # 根据行号获取行
        if row:  # 如果行存在
            app = []  # 一行的内容
            for i in range(len(colnames)):  # 一列列地读取行的内容
                app.append(row[i])
            list.append(app)  # 装载数据
    return list


managerList = [
]


# 主函数
def main():
    tables = excel_table_byname()
    for a, row in enumerate(tables):
        # 当第4位置 存在内容就是县
        if len(row[3]) > 0:
            film_dict = {}

            film_dict['C0'] = a
            film_dict['PLACECODE'] = str(int(row[0]))
            # film_dict['PLACENAME'] = row[3]
            film_dict['PLACENAME'] = str(row[3]).replace(' ', '')
            # print(str(a))
            # print(type(film_dict['PLACENAME']))
            managerList.append(film_dict)


if __name__ == "__main__":
    main()
    savexml(managerList, 'area2.xml')
    print(managerList)
    print(len(managerList))

