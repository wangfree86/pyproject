# -*- coding: utf-8 -*- 
import xdrlib, sys
import xlrd
import xml.dom.minidom


# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
def savexml(managerList,name):
    doc = xml.dom.minidom.Document()
    # 创建一个根节点Managers对象
    root = doc.createElement('ROWDATA')
    # 设置根节点的属性
    # root.setAttribute('company', 'xx科技')
    # root.setAttribute('address', '科技软件园')
    # 将根节点添加到文档对象中
    doc.appendChild(root)
    for i in managerList:
        nodeManager = doc.createElement('ROW')
        nodeName = doc.createElement('C0')
        # 给叶子节点name设置一个文本节点，用于显示文本内容
        nodeName.appendChild(doc.createTextNode(str(i['C0'])))

        nodeAge = doc.createElement("PLACECODE")
        nodeAge.appendChild(doc.createTextNode(str(i["PLACECODE"])))

        nodeSex = doc.createElement("PLACENAME")
        nodeSex.appendChild(doc.createTextNode(str(i["PLACENAME"])))

        # 将各叶子节点添加到父节点Manager中，
        # 最后将Manager添加到根节点Managers中
        nodeManager.appendChild(nodeName)
        nodeManager.appendChild(nodeAge)
        nodeManager.appendChild(nodeSex)
        root.appendChild(nodeManager)
    # 开始写xml文档
    fp = open('c:\\'+name, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


# 打开excel文件
def open_excel(file='test.xlsx'):
    # try:
    data = xlrd.open_workbook(file)
    return data
    # except Exception,e:
    #     print str(e)


# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
def excel_table_byname(file='address.xls', colnameindex=0, by_name=u't_address'):
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
        type = row[3]
        if type == 1:
            film_dict = {}
            film_dict['C0'] = a
            film_dict['PLACECODE'] = row[1]
            film_dict['PLACENAME'] = row[0]
            if len(row[1])>2:

                managerList.append(film_dict)
            else:
                print(row[1]+row[0])
        # managerList.append(row)
        #     print(row)


if __name__ == "__main__":
    main()
    savexml(managerList,'pcity.xml')
    print(managerList)
    print(len(managerList))
