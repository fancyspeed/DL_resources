#coding: utf-8
import requests as req
import time
import re
import json

wenshu_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer':'http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+%E5%8C%97%E4%BA%AC%E5%B8%82%E5%B9%B3%E8%B0%B7%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2+++%E5%9F%BA%E5%B1%82%E6%B3%95%E9%99%A2:%E5%8C%97%E4%BA%AC%E5%B8%82%E5%B9%B3%E8%B0%B7%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Cookie': 'FSSBBIl1UgzbN7N80S=XZ2p.dtq9UznRwRynW7vxQxFe8HNhtjKgy0gqQSLhR.5suBlrzJINmRvw5NgoDrC; _gscu_1049835508=82859416ueqjdr14; _gscbrs_1049835508=1; Hm_lvt_9e03c161142422698f5b0d82bf699727=1482859419; Hm_lpvt_9e03c161142422698f5b0d82bf699727=1482859419; ASP.NET_SessionId=enpn1k1waalcinnmkijbtkoe; _gsref_2116842793=http://wenshu.court.gov.cn/; Hm_lvt_3f1a54c5a86d62407544d433f6418ef5=1482857491; Hm_lpvt_3f1a54c5a86d62407544d433f6418ef5=1483281477; _gscu_2116842793=828574921hhs7q31; _gscs_2116842793=t8328134677t4iy20|pv:4; _gscbrs_2116842793=1; FSSBBIl1UgzbN7N80T=1hN5PNHp2sG7WKI5vIDXy_H96cMWq9z4wAHRl1cQr0TwSp7B0N20mVQnYbFEjcSEi39XaYsEo87aJMsd10PdC8xVZMErOesLNMQwkly1lp9g_jmI1zOWD6T8MtRCGXuxnpSttRJiirCtadpHS7a0UkxweAczCMYhHzx6Ac8aSrx5jjPBbcwj8rHXL8BA35h3gWFHBtZAOIa82UQYHpVHLzusWhAn4R_2sVN0ijRsH_skeLhwArbtHIFITNmNTLAD1SOX_vnUKRZhTLsCTYq2dGDgE8rsa3v3mGZgz4Oq7cgDvsUngKdsHCg7YzMI8aB1VxG'
    }
wenshu_index_url = 'http://wenshu.court.gov.cn/List/ListContent?MmEwMD=1JL8_BiSeYfWVA88dRoifZilBlF73P7MmKiyQVkZRn0eNUzH7B9Vw1w1JGMLnlaLK82iLs1LI3zAYw1ItnOIX3ECeXBhEzQtAuza6WJhtAEQ4jnWRV253.84W6cxaVDX4Ilo3kmW6NCPJQiJVz5YsJO8gzm5HgASIvERAylBMxpW2t8SYepk2IBmHyzVvKwONuf4fEj8qQOIRrSbCvmvjarE1VeemkH0kA_y_zCvcOpHXNROqYShJJUs_uma.yjI9b0XZgIKCYV8H.wDEtPUlqfkAOmiRadXcPgJCVy4y1QIo6kIj0QNTmOI6ObimpbN8fqBrl2iZc6QbrhDGu8CuVvkMC3.mKzh3UH79GaF6rA5Zgsf_t9yKXAsCB39uRwPsB0' 

def wenshu_index_iter(param,max_id=100000):
    pageSize=20
    Index=1
    SleepNum = 3
    dates=[]
    titles=[]
    nums=[]

    while Index < max_id/pageSize + 1:
        data={'Param':param,
            'Index': Index,
            'Page':pageSize,
            'Order':'裁判日期',
            'Direction':'desc'}
        r = req.post(wenshu_index_url, headers=wenshu_headers, data = data)
        if r.status_code != 200: 
            break
        for d in json.loads(r.json()): 
            yield d
        time.sleep(SleepNum)
        Index += 1

