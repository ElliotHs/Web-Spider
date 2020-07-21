#!/usr/bin/env python
# coding: utf-8

# In[91]:


url='https://www.rongrong.cn/search/biaozhun/c-1001?keyword=%E9%9B%B7%E8%BE%BE&pageNo=1&pageSize=459' #需要获取的数据页面

from selenium import webdriver#导入库
from bs4 import BeautifulSoup
import time
import re
def main():
    browser = webdriver.Chrome()#声明浏览器   
    browser.get(url)#打开浏览器预设网址
    time.sleep(5)#强制等待浏览器页面加载
    html = browser.page_source #获取页面源代码
    return html


#添加正则表达式
findNum = re.compile(r'<span class="search-bz-conts-tips">(.*?)</span>')
findLink = re.compile(r'<a href="(.*?)" target="_blank">',re.S)
findName = re.compile(r'<span class="search-bz-conts-tips">.*?</span>(.*?\S)\s*</div>',re.S)
findTime = re.compile(r'<div>(\d.*?)</div>')
findOgan = re.compile(r'<div>来源：.*?<div>(.*?)</div>',re.S)
findState = re.compile(r'<span class="search-bz-tips.*">(.*?)</span>')
findSummary = re.compile(r'<div class="previewTextbox-text">.*?适用范围：(.*?)</div>',re.S)
def getData(html):
    soup = BeautifulSoup(html,"html.parser")#使用BeautifulSoup对页面进行解析
    results = soup.find_all('div',class_ = 'searchall-bz-list-box')
    dataList = []
    for item in results:
        data = []
        item = str(item)
#         print(item)
        num = re.findall(findNum,item)
        link = re.findall(findLink,item)
        name = re.findall(findName,item)
        time = re.findall(findTime,item)
        ogan = re.findall(findOgan,item)
        state = re.findall(findState,item)
        summary = re.findall(findSummary,item)
        if len(num) != 0:
            num = num[0]
            print(num)
            data.append(num)
        if len(link) != 0:
            link = link[0]
            print(link)
            data.append(link)
        if len(name) != 0:
            name = name[0]
            name = name.replace('<span style="color: #ff664c">','')
            name = name.replace('</span>','')
            print(name)
            data.append(name)
        if len(time) != 0:
            print(time)
            data.append(time[0])
            data.append(time[1])
        else:
            data.append(' ')
            data.append(' ')
        if len(ogan) != 0:
            ogan = ogan[0]
            print(ogan)
            data.append(ogan)
        if len(state) != 0:
            state = state[0]
            data.append(state)
            print(state)
        if len(summary)!=0:
            summary = summary[0]
            summary = summary.replace('<span style="color: #ff664c">','')
            summary = summary.replace('</span>','')
            if(summary == "0.0"):
                summary == ' '
            data.append(summary)
            print(summary)
            dataList.append(data)
    return dataList



filepath = r'.\国军标准\GJB.csv'
def saveData():
    f = open(filepath,'w',newline='',encoding ="utf-8-sig")
    csv_writer = csv.writer(f)
    for item in csvfile:
        csv_writer.writerow(item)
    f.close()


# In[168]:

if __name__ == '__main__':

	html=main()

	import csv
	import os
	dataList = getData(html)

	#暂存数据
	csvfile = []
	csvfile.append(['标准号','链接','标准名称','发布日期','实施日期','来源单位','状态','适用范围'])
	for data in dataList:
	    csvfile.append(data)

	#保存数据
	saveData()






