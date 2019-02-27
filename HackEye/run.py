# coding = utf-8
# author:PpBibo


import argparse
import threading
import os,re,sys,time
import requests
import xlrd
import smtplib
from email.mime.text import MIMEText
from email.header import Header




WVS_CONSOLE_PATH = "C:\Program Files (x86)\Acunetix\Web Vulnerability Scanner 10"

ReportFile = "output"

nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}




def Connection(domain):
    '''
        检测可否与网站通信
    :param domain:
    :return:
    '''

    try:

        print('[Tps] Running, please wait...\n[Tps] Checking if the website can communicate normally...')

        conn = requests.get(domain, headers=header, timeout=3)

        if conn:
            print(conn.status_code)

            pass

    except:

        print('[-] Communication error with this website')

        sys.exit(0)  # 正常退出此程序



def sendmail():

    '''

     邮件发送

    :return:
    '''

    sender = 'test@163.com'

    password = '******'

    receiver = '1443827388@qq.com'

    words = '''

    <p> 扫描完成 </p>
    <p> 时间 %s </p>

    ''' % (nowTime)

    # msg = MIMEText('Test 这是一封测试邮件', 'plain', 'utf-8')

    msg = MIMEText(words, 'html', 'utf-8')

    msg['from'] = sender

    msg['to'] = receiver

    subject = 'Scan Complete'

    msg['subject'] = Header(subject, 'utf-8')

    try:
            conn = smtplib.SMTP('smtp.163.com')

            conn.login(sender, password)

            conn.sendmail(sender,receiver,msg.as_string())

            conn.quit()

            print("[+] Send mail ok!!!")

    except smtplib.SMTPException as e:

            print("[-] Error: send mail error\n{}".format(e))





def Bat_Aut_Scanning(DomainXlsFile_Name):
    '''
        批量扫描策略
    :param DomainXlsFile_Name:
    :return:
    '''
    try:

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

            # 正则匹配域名作为导出的报告文件名称
            saveFile_PATH = re.sub("http://", "", domain)

            if "https" in saveFile_PATH:
                saveFile_PATH = re.sub("https://", "", domain)

            try:

                # 进入 wvs_console.exe 目录
                os.chdir(WVS_CONSOLE_PATH)

            except:
                print("[!] error:{} path not exits".format(WVS_CONSOLE_PATH))
                sys.exit(0)

            print(saveFile_PATH)

            time.sleep(2)

            try:

                ''' 
                Dhuang 个人指定的扫描配置
                Default 默认扫描配置

                python3 demo.py -c "Batscan" -d "demo.xls"
                '''

                os.system(
                    "color b && wvs_console.exe /Scan %s /Profile Dhuang /Verbose /SaveFolder C:\\report\\%s /SaveLogs /GenerateReport /ReportFormat pdf --ScanningMode=Heuristic --RobotsTxt=TRUE --ForceFetchDirindex=TRUE --EnablePortScanning=TRUE --ManipHTTPHeaders=TRUE --ToolTimeout=15 --RestrictToBaseFolder=FALSE --UseSensorDataFromCrawl=No" % (
                    domain, saveFile_PATH))

            except Exception as e:

                print("[!] error message: \n{}".format(e))

    except:

        pass

    print('扫描全部完成 当前时间: {}'.format(nowTime))


def SingleScanning(domain):
    '''
        单个扫描策略
    :param domain:
    :return:
    '''

    # 正则匹配域名作为导出的报告文件名称
    saveFile_PATH = re.sub("http://", "", domain)

    if "https" in saveFile_PATH:
        saveFile_PATH = re.sub("https://", "", domain)

    try:

        os.chdir(WVS_CONSOLE_PATH)

    except:
        print("[!] error:{} path not exits".format(WVS_CONSOLE_PATH))
        sys.exit(0)

    print(saveFile_PATH)

    time.sleep(2)

    try:

        ''' 
        Dhuang 个人指定的扫描配置
        Default 默认扫描配置

        python3 demo.py -c "DesScan" -u "http://www.baidu.com"

        '''

        os.system(
            "color b && wvs_console.exe /Scan %s /Profile Dhuang /Verbose /SaveFolder C:\\report\\%s /SaveLogs /GenerateReport /ReportFormat pdf --ScanningMode=Heuristic --RobotsTxt=TRUE --ForceFetchDirindex=TRUE --EnablePortScanning=TRUE --ManipHTTPHeaders=TRUE --ToolTimeout=15 --RestrictToBaseFolder=FALSE --UseSensorDataFromCrawl=No" % (
            domain, saveFile_PATH))

    except Exception as e:
        print("[!] error message: \n{}".format(e))

    print('扫描任务完成 当前时间: {}'.format(nowTime))


def scanDir():


    try:

        os.system("python3 scandir.py")

    except Exception as e:
        print("[-] scandir error:\n{} ".format(e))
        sys.exit(0)

def main():

    if Choice == "BatScan":       # 批量扫描策略

        try:

            t = threading.Thread(target=Bat_Aut_Scanning, args=(DomainXlsFile_Name,))

            t.start()

        except Exception as e:

            print("[!] error message: \n{}".format(e))

        time.sleep(0.5)

        sendmail()



    elif Choice == "DesScan":       # 单个扫描策略

        try:

            Connection(domain)
            SingleScanning(domain)
            sendmail()

        except Exception as e:

            print("[!] error message: \n{}".format(e))

    elif Choice == "ScanDir":       # 扫描敏感目录

        scanDir()
        sendmail()

    else:

        pass



if __name__ == '__main__':

    try:

        parse = argparse.ArgumentParser()
        parse.add_argument('-c', '--choice', dest="Choice", type=str,help="Choice a scanning strategy")
        parse.add_argument('-d', '--DomainXlsFile', dest="DomainXlsFile_Name", default="domain.xls", type=str,help="Import XLS file name")
        parse.add_argument('-u', '--domain',dest="domain",type=str ,help="Please submit a domain name")
        parse.add_argument('-e', '--dicname', dest="DIC_Name", type=str, help="Please submit DIC Name")
        args = parse.parse_args()
        Choice = args.Choice
        DomainXlsFile_Name = args.DomainXlsFile_Name
        domain = args.domain
        DIC_Name = args.DIC_Name

    except:
        print("[Tips] Drop parameter")

    main()