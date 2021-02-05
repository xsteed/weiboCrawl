'''
Descripttion: 爬虫爬取微博热搜并存储于mysql数据库
version: 1.0
Author: LJZ
Date: 2020-12-02 20:50:47
LastEditTime: 2021-02-05 16:45:36
'''
import requests
import pymysql
import time

from lxml import etree


""" 爬取微博热搜榜 """

def getHTMLText(url):
    """ 获取微博网页数据 """
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            }

        r = requests.get(url,headers = headers)
        
        """ 如果状态码不是200 则会引起HTTPerror异常 """
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def insert(value):
    """ 将数据插入mysql """

    sql = "INSERT INTO hot_list(name,url,scores) values(%s,%s,%s)"
    
    try:
        cursor.execute(sql,value)
        db.commit()
        print('插入数据成功')
    except:
        db.rollback()
        print("插入数据失败")


def delete(mycursor):
    """ 删除mysql的数据 """
    
    sql = "DELETE FROM hot_list"
    mycursor.execute(sql)



if __name__ == "__main__":
    
    # 数据库配置
    dbConfig = {
        'host':'localhost',
        'user':'root',
        'password':'root',
        'db':'data'
    }

    url = "https://s.weibo.com/top/summary?cate=realtimehot"
    # print(getHTMLText(url))

    # 连接mysql
    db = pymysql.connect(host = dbConfig['host'], user=dbConfig['user'], password=dbConfig['password'], port=3306, db=dbConfig['db'])
    cursor = db.cursor()

    # 定时任务5s
    while(True):

        web_data = getHTMLText(url)
        # print(web_data)
        
        html = etree.HTML(web_data)
        html_title = html.xpath("//*[@id='pl_top_realtimehot']/table/tbody/tr/td[2]/a/text()")
        html_url = html.xpath("//*[@id='pl_top_realtimehot']/table/tbody/tr/td[2]/a/@href")
        html_hot = html.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]/span/text()')

        # 删除数据库原有数据
        delete(cursor)

        for i in range(len(html_hot)):
            print(html_title[i+1]," ",r'https://s.weibo.com'+html_url[i+1]," ",html_hot[i])
            
            value = (html_title[i+1],r'https://s.weibo.com'+html_url[i+1],html_hot[i])
            insert(value)

        time.sleep(5)

    db.close()

