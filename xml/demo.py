import xml.dom.minidom


#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
def savexml(managerList):

    doc = xml.dom.minidom.Document()
    #创建一个根节点Managers对象
    root = doc.createElement('Managers')
    #设置根节点的属性
    # root.setAttribute('company', 'xx科技')
    # root.setAttribute('address', '科技软件园')
    #将根节点添加到文档对象中
    doc.appendChild(root)
    for i in managerList :
        nodeManager = doc.createElement('Manager')
        nodeName = doc.createElement('name')
        #给叶子节点name设置一个文本节点，用于显示文本内容
        nodeName.appendChild(doc.createTextNode(str(i['name'])))

        nodeAge = doc.createElement("age")
        nodeAge.appendChild(doc.createTextNode(str(i["age"])))

        nodeSex = doc.createElement("sex")
        nodeSex.appendChild(doc.createTextNode(str(i["sex"])))

        #将各叶子节点添加到父节点Manager中，
        #最后将Manager添加到根节点Managers中
        nodeManager.appendChild(nodeName)
        nodeManager.appendChild(nodeAge)
        nodeManager.appendChild(nodeSex)
        root.appendChild(nodeManager)
    #开始写xml文档
    fp = open('c:\\Manager.xml', 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")

managerList = [{'name' : 'joy',  'age' : 271, 'sex' : '女'},
               {'name' : 'tom', 'age' : 310, 'sex' : '男'},
               {'name' : 'ruby', 'age' : 29, 'sex' : '女'}
               ]

#主函数
def main():
    savexml(managerList)

if __name__=="__main__":
    main()