# -*- coding:utf-8 -*-

# from apscheduler.schedulers.blocking import BlockingScheduler
import datetime, time
import os
import xlrd
from email.mime.text import MIMEText
from email.header import Header
import smtplib




# File_path ="D:\\Program Files (x86)\\IBM\\AppScan Standard"
# Save_path = "E:\\report"
Save_path = "E:\\new_report"

File_path = "/Volumes/[C] 封印的(Windows 7).hidden/Program Files (x86)/Acunetix/Web Vulnerability Scanner 10/"

def send():
    sender = '*********'
    password = '********'
    receiver = '***********'  # 收件人
    words = "<p>test</p>"
    msg = MIMEText(words, 'html', 'utf-8')
    msg['from'] = sender
    msg['to'] = receiver
    subject = '扫描报告'
    msg['subject'] = Header(subject, 'utf-8')
    try:
        conn = smtplib.SMTP('smtp.exmail.qq.com')
        conn.login(sender, password)
        conn.sendmail(sender, receiver, msg.as_string())
        conn.quit()
        print("邮件成功")
    except smtplib.SMTPException:
        print("未发送成功")

# send()


def scan():

    # send()
    data = xlrd.open_workbook("E:\\test_new.xls")
    table = data.sheets()[0]
    nrows = table.nrows
    # ncols = table.ncols
    a = os.chdir(File_path)
    print(a)
    for i in range(nrows):
        if i == 0:      # 跳过第一行
            continue
        url = table.row_values(i)[0]
        print(url)
        file_name = url[0:4]
        time.sleep(3)
        try:
            os.chdir(File_path)
            print(os.listdir())

            # os.system('AppScanCMD /e /starting_url %s /policy_file D:\\test.policy /rt pdf /rf D:\\www.pdf')
            os.system('wvs_console.exe /Scan %s /Profile Test /loginseq E:\\login\\ 172.16.5.57 /SaveFolder E:\\www\\%s --ScanningMode=Heuristic --ToolTimeout=15 /GenerateReport /ReportFormat pdf' % (url,file_name))
            # os.system('wvs_console.exe /Scan %s /Profile Default /SaveFolder \\%s --ScanningMode=Heuristic --RobotsTxt=TRUE --ForceFetchDirindex=TRUE --ToolTimeout=15 /SaveLogs %s /GenerateReport /ReportFormat pdf' % (url,Save_path,file_name))
            os.system('wvs_console.exe -h')
        except:

            pass

        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))

scan()

# sched = BlockingScheduler()

# cron 周期性计划
# 当前任务会在每月的第三个周五的22:00执行
# sched.add_job(scan, 'cron', month='1-12', day='3rd fri', hour='22')
# sched.start()




