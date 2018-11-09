# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd

#打开excel文件
def open_excel(file= 'tt.xlsx'):
    # try:
        data = xlrd.open_workbook(file)
        return data
    # except Exception,e:
    #     print str(e)

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
def excel_table_byname(file= 'tt.xlsx', colnameindex=0, by_name=u'1-3'):
    all=0;
    jia=0;
    tiaoxiu=0;
    data = open_excel(file) #打开excel文件
    table = data.sheet_by_name(by_name) #根据sheet名字来获取excel中的sheet
    nrows = table.nrows #行数 
    colnames = table.row_values(colnameindex) #某一行数据 
    list =[] #装读取结果的序列
    for rownum in range(0, nrows): #遍历每一行的内容
        row = table.row_values(rownum) #根据行号获取行
        if row: #如果行存在
            app = [] #一行的内容
            for i in range(len(colnames)): #一列列地读取行的内容
                app.append(row[i])
            # if app[1] == '冯伟':
            # if app[1] == '':
            if app[1] == '王凯':
                list.append(app) #装载数据 3.3.5  156
                if app[3] == '加班':
                    all=all+app[2]
                    jia=jia+app[2]
                if app[3] == '调休':
                    # print("调休--------"+by_name+"="+app[0]+str(app[2]))
                    all=all-app[2]
                    tiaoxiu=tiaoxiu+app[2]

    print("加班"+by_name+"="+str(jia))
    print("调休"+by_name+"="+str(tiaoxiu))
    print("最后时间"+by_name+"="+str(all))
    print('-------------')
    return all
    return list

#主函数
def main():
    # tables = excel_table_byname('tt.xlsx',0,'1-3')
    a=excel_table_byname('tt.xlsx',0,'1-3')+excel_table_byname('tt.xlsx',0,'4-6')+excel_table_byname('tt.xlsx',0,'7-9')+excel_table_byname('tt.xlsx',0,'10-12')
    print ('------------'+str(a))
    # tables = excel_table_byname('tt.xlsx',0,'1-3')
    # tables = excel_table_byname('tt.xlsx',0,'4-6')
    # tables = excel_table_byname('tt.xlsx',0,'7-9')
    # tables = excel_table_byname('tt.xlsx',0,'10-12')
    # for row in tables:
    #     print (row)

if __name__=="__main__":
    main()