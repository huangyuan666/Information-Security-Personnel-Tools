# coding = utf-8


import requests
import random
import os
import xlrd


DomainList = []
error=[]
headersList=[]
save=[]


def DomainSet(DomainXlsFile_Name):

    ''' 域名文件加载 '''

    data = xlrd.open_workbook(DomainXlsFile_Name)
    table = data.sheets()[0]
    nrows = table.nrows  # 获取行数
    ncols = table.ncols  # 获取列数

    for i in range(nrows):

        if i == 0:  # 跳过第一行

            continue

        domain = table.row_values(i)[0]

        if "http" not in domain:

            domain = "http://" + domain

        if domain.endswith("/") == False:

            domain = domain + "/"

        DomainList.append(domain)



def errors():

    ''' 错误文件过滤'''

    lv=open('file/error.txt','r',encoding='utf-8')
    for e in lv.readlines():
        qcsw="".join(e.split('\n'))
        error.append(qcsw)


def header_text():

    headers_file = open('file/user-agent.txt','r')
    for item in headers_file.readlines():
        wq = "".join(item.split('\n'))
        headersList.append(wq)


def exploit():

    dics = os.listdir('Dictionary_dic')

    ran_header = {'user-agent': headersList[random.randint(0, int(len((headersList)) - 1))]}

    for file_name in dics:
        dp = open('{}'.format('Dictionary_dic/' + file_name),'r',encoding='gbk')
        for dic_data in dp.readlines():
            route = "".join(dic_data.split('\n'))
            # print(route)
            for u in DomainList:
                url = '{}'.format(u) + route    # 拼接好的域名

                try:
                    requet = requests.get(url=url,headers=ran_header,timeout=3,allow_redirects=False)   # 不允许重定向

                    for err in error:

                        # 过滤错误信息
                        if requet.status_code == 200 and not err in requet.text:

                            success = '[+] code:{} url : {} '.format(requet.status_code,requet.url)

                            if success in save:continue
                            save.append(success)
                            print(success)

                        else:
                            notFind = '[-] Not existent dimain :{}'.format(requet.url)
                            print(notFind)

                except Exception as e:

                    # pass
                    print('[-] Error {}'.format(e))



    # 判断save列表存在数据则写入到 save.txt 文件
    if len(save) > 0:
        od = open('output/report/save.txt','w')
        od.close()

        od = open('output/report/save.txt','r')
        for success_item in save:  # 循环save列表里面的数据写入到save.txt
            print(success_item,file=open('output/report/save.txt','a'))




def dirscan_main(DomainXlsFile_Name):

    DomainSet(DomainXlsFile_Name)
    print('[+] Domain Name List Load completion')
    print(' ')

    errors()
    print('[+] The Error filter file is loaded')
    print(' ')

    header_text()
    print('[+] Headers User-Agent List Load completion')
    print(' ')


    print('[*] Start scanning...')
    print(' ')
    exploit()



if __name__ == '__main__':

    dirscan_main('domain.xls')