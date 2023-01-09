import urllib.request       #导入urllib库

url = urllib.request.urlopen("https://www.qinghuawang.net/a/292202.html")        #需要抓取数据的网站
data = url.read()
dt1 = open("E:/GetDataByPy/2.xls","wb")       #xls表的位置，会自动生成xls表
dt1.write(data)   #将数据写入D:/Code/data/2.xls表中
dt1.close()
print(data)