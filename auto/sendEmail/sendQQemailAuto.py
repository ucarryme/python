# -*- coding: UTF-8 -*-
'''
@Project ：PM_Project 
@File    ：SendLoveMail.py
@IDE     ：PyCharm 
@Author  ：Manba_77
@Date    ：2022/9/30 23:36 
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
from numpy import true_divide
import pymysql
import random
import requests
from xpinyin import Pinyin
from lxml import etree
import time


class love_mail():
    def __init__(self):
        # 读取参数文件
        with open('E:/study/Learning Python/auto/sendEmail/config.txt', 'r', encoding='utf-8') as f:
            read_result = f.readlines()
        # print(read_result)
        for result in read_result:
            # 发件人名字
            if 'Sender_name' in result:
                self.Sender_name = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'发件人名字:{self.Sender_name}')
            # 发件人名字
            if 'Attn_name' in result:
                self.Attn_name = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'收件人名字:{self.Attn_name}')
            # 邮件标题
            if 'Subject' in result:
                self.Subject = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'邮件标题:{self.Subject}')
            # 发件方QQ邮箱
            if 'Sender_mail' in result:
                self.Sender_mail = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'发件方QQ邮箱:{self.Sender_mail}')
            # 接收方QQ邮箱,可以写多个
            if 'Receive_mail' in result:
                self.Receive_mail = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'接收方QQ邮箱:{self.Receive_mail}')
            # QQ邮箱的授权码
            if 'Authorization_code' in result:
                self.Authorization_code = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'QQ邮箱的授权码:{self.Authorization_code}')
            # 城市
            if 'City' in result:
                self.City = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'城市:{self.City}')
            # 在一起的时间
            if 'Together_time' in result:
                self.Together_time = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'在一起的时间:{self.Together_time}')
            # 女孩的生日时间
            if 'Girl_bday' in result:
                self.Girl_bday = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'女孩的生日时间:{self.Girl_bday}')
            # 男孩的生日时间
            if 'Boy_bday' in result:
                self.Boy_bday = eval(result.split(' = ')[1].replace('\n', ''))
                print(f'男孩的生日时间:{self.Boy_bday}')

    # 获取现在时间  '2022-9-28 星期二'self.time_now
    def get_time(self):
        # 现在的时间    年-月-日
        now = datetime.datetime.now().strftime("%Y-%m-%d").replace('-', '—')
        year = eval(now[:4])
        if now[5:6] == '0':
            month = eval(now[6:7])
        else:
            month = eval(now[5:7])

        if now[8:9] == '0':
            day = eval(now[9:])
        else:
            day = eval(now[8:])

        week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        # 现在周几
        weekday = week_list[datetime.date(year, month, day).weekday()]
        # 拼接时间      年-月-日 周几
        self.time_now = now + '&nbsp;&nbsp;&nbsp;&nbsp;' + weekday
        # return time_now

    # 获取天气气温  天气self.weather  最低气温self.low_air   最高气温self.high_air
    def get_weather_air(self):
        p = Pinyin()
        city = ''.join(p.get_pinyin(self.City).split('-'))
        url = 'https://www.tianqi.com/{}/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        response = requests.get(url=url.format(city), headers=headers)
        text = response.text

        html = etree.HTML(text)
        # 天气
        self.weather = html.xpath('//dd[@class="weather"]/span/b/text()')[0]
        air = html.xpath('//dd[@class="weather"]/span/text()')[0]
        self.low_air = air.split(' ~ ')[0] + '℃'
        self.high_air = air.split(' ~ ')[1]

    # 计算相恋的时间  [天数,年,月,日]
    def count_love_time(self):
        # 在一起的时间
        start_data = self.Together_time
        # print(f'开始时间{start_data}')

        # 现在时间
        now_data = datetime.datetime.now().strftime("%Y-%m-%d")
        # print(f'现在时间{now_data}')

        # 一共的天数
        days_count = (datetime.datetime(int(now_data[:4]), int(now_data[5:7]), int(now_data[8:])) - datetime.datetime(int(start_data[:4]), int(start_data[5:7]), int(start_data[8:]))).days
        print(f'已经在一起{days_count}天')
        print(f'{days_count}')

        # 计算年份
        # print('年份：')
        year_1 = eval(start_data[:4])
        # print(year_1)

        year_2 = eval(now_data[:4])
        # print(year_2)

        # 计算月份
        # print('月份：')
        if start_data[5:6] == '0':
            month_1 = eval(start_data[6:7])
        else:
            month_1 = eval(start_data[5:7])
        # print(month_1)

        if now_data[5:6] == '0':
            month_2 = eval(now_data[6:7])
        else:
            month_2 = eval(now_data[5:7])
        # print(month_2)

        # 计算日
        # print('日：')
        if start_data[8:9] == '0':
            day_1 = eval(start_data[9:])
        else:
            day_1 = eval(start_data[8:])
        # print(day_1)

        if now_data[8:9] == '0':
            day_2 = eval(now_data[9:])
        else:
            day_2 = eval(now_data[8:])
        # print(day_2)

        # print('-' * 30)
        year_count = year_2 - year_1
        if month_2 - month_1 > 0:
            month_count = month_2 - month_1
            if day_2 - day_1 >= 0:
                day_count = day_2 - day_1
            else:
                day_count = day_1 - day_2
                month_count = month_count - 1
        elif month_2 - month_1 == 0:
            if day_2 - day_1 >= 0:
                day_count = day_2 - day_1
                month_count = 0
            else:
                day_count = day_1 - day_2
                year_count -= 1
                month_count = 11
        else:
            year_count -= 1
            month_count = month_1 - month_1
            if day_2 - day_1 >= 0:
                day_count = day_2 - day_1
            else:
                day_count = day_1 - day_2
                month_count -= 1

        print(f'{year_count}年{month_count}月{day_count}天')

        return [days_count, year_count, month_count, day_count]

    # 下一个纪念日还有多少天 self.verse
    def next_verse_days(self):
        start_data = self.Together_time
        # 现在时间
        now_data = datetime.datetime.now().strftime("%Y-%m-%d")
        # print(f'现在时间{now_data}')
        mounth_day = start_data[4:]
        y = int(now_data[:4])

        while True:
            year = str(y)
            next_data = year + mounth_day
            # print(f'下一个时间{next_data}')

            # 一共的天数
            days_count = (datetime.datetime(int(next_data[:4]), int(next_data[5:7]),int(next_data[8:])) - datetime.datetime(int(now_data[:4]),int(now_data[5:7]),int(now_data[8:]))).days

            if days_count >= 0:
                self.verse = days_count
                print(f'距离下一个周年纪念日还有{days_count}天')
                break
            y += 1

    # 距离下一个生日还有多少天
    def next_bday_days(self, bday_day):

        # 现在时间
        now_data = datetime.datetime.now().strftime("%Y-%m-%d")
        # 生日的月-日
        mounth_day = bday_day[4:]

        y = int(now_data[:4])

        while True:
            year = str(y)
            next_data = year + mounth_day
            # print(f'下一个时间{next_data}')

            # 一共的天数
            days_count = (datetime.datetime(int(next_data[:4]), int(next_data[5:7]),int(next_data[8:])) - datetime.datetime(int(now_data[:4]),int(now_data[5:7]),int(now_data[8:]))).days

            if days_count >= 0:
                print(f'距离下一个生日还有{days_count}天')
                return days_count
            y += 1

    # 获取每日语录
    def get_love_sayings(self):
        with open('E:/study/Learning Python/auto/sendEmail/love_ana.txt', 'r', encoding='utf-8') as f:
            l_a = f.readlines()
        l = len(l_a)

        m = random.choice([i for i in range(l)])

        love_sayings = eval(l_a[m].replace('\n', ''))
        print(love_sayings)
        return love_sayings

    # 发送
    def send_mail(self, mail_msg):
        # 邮件内容
        message = MIMEText(mail_msg, 'html', 'utf-8')

        # 发件人的名字，可以自由写
        message['From'] = Header(self.Sender_name, 'utf-8')

        # 发件人名字，可以自由填写
        message['To'] = Header(self.Attn_name, 'utf-8')

        # 邮件标题
        message['Subject'] = Header(self.Subject, 'utf-8')

        # 使用QQ邮箱的服务，发送邮件
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 发送的QQ邮箱账号, QQ邮箱的授权码
        smtpObj.login(self.Sender_mail, self.Authorization_code)
        # 发送方QQ邮箱账号, 接受方QQ邮箱账号
        smtpObj.sendmail(self.Sender_mail, self.Receive_mail, message.as_string())
        smtpObj.quit()
        print('邮箱发送成功')

    # 启动
    def run(self):
        Subject = self.Subject                               # 标题
        self.get_time()                                      # 获取现在日期
        Time_now = self.time_now                             # 时间
        City = self.City                                     # 城市
        self.get_weather_air()                               # 获取天气
        Weather = self.weather                               # 天气
        Low_air = self.low_air                               # 最低温度
        High_air = self.high_air                             # 最高温度
        count_love_time = self.count_love_time()
        Days, Years, Mounts, ds = count_love_time
        self.next_verse_days()
        Verse = self.verse                                  # 周年纪念日
        G_name = self.Attn_name                             # 女孩名字
        G_days = self.next_bday_days(self.Girl_bday)        # 女孩生日倒计时
        B_name = self.Sender_name                           # 男孩名字
        B_days = self.next_bday_days(self.Boy_bday)         # 男孩生日倒计时
        Say_en, Say_ch = self.get_love_sayings()            # 每日语录
        Sign_name = self.Sender_name

        # 发送的邮件内容
        mail_msg = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>早上好</title>
</head>
<body>
<div style="border: 1px solid white; width: 400px; height: 650px; margin: 0 auto; border-radius:5%; background-color:#FFA500;">
    <p style="color: hotpink;margin-top: 30px; margin-left: 15px;">{Subject}</p>
    <p style="color: #00FA9A;margin: 15px">{Time_now}</p>
    <p style="margin: 15px">城市: <span style="color: #FFA500">{City}</span></p>
    <p style="margin: 15px">天气: <span style="color: dodgerblue">{Weather}</span></p>
    <p style="margin: 15px">最低气温: <span style="color: lime">{Low_air}</span></p>
    <p style="margin: 15px">最高气温: <span style="color: orangered">{High_air}</span></p>
    <p style="margin: 15px">今天是我们相恋的第<span style="color:#00BFFF">{Days}</span>天</p>
    <p style="margin: 15px">我们已经在一起<span style="color: hotpink">{Years}</span>年<span style="color: hotpink">{Mounts}</span>个月<span style="color: hotpink">{ds}</span>天</p>
    <p style="margin: 15px">距离下一个周年纪念日还有<span style="color: greenyellow">{Verse}</span>天</p>
    <p style="margin: 15px">距离<span style="color: gold">{G_name}</span>的生日还有<span style="color: yellow">{G_days}</span>天</p>
    <p style="margin: 15px">距离<span style="color: black">{B_name}</span>的生日还有<span style="color: turquoise">{B_days}</span>天</p>
    <p style="margin-top: 30px; margin-left: 15px; margin-bottom:7px; color: #27ff28; font-size: 15px">{Say_en}</p>
    <p style="margin-top: 0; margin-left: 15px; color: #27ff28;font-size: 15px">{Say_ch}</p>
    <p style="margin-top: 50px; margin-left: 290px;color: aqua">——{Sign_name}</p>
</div>
</body>
</html>'''

        # 发送
        self.send_mail(mail_msg)

if __name__ == '__main__':
    with open('E:/study/Learning Python/auto/sendEmail/config.txt', 'r', encoding='utf-8') as f:
        read_result = f.readlines()
    for result in read_result:
        if 'Send_time' in result:
            Send_time = eval(result.split(' = ')[1].replace('\n', ''))

            while True:
                time_now = time.strftime("%H-%M", time.localtime())
                print(time_now)
                #if time_now == Send_time:
                if True:
                    LM = love_mail()
                    LM.run()
                    print('*'*100)
                    time.sleep(60)
                break
            break
        
         
            
