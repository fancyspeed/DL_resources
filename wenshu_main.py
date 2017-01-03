#coding: utf-8
from wenshu_spider import wenshu_index_iter

wenshu_index_params = ['案件类型:刑事案件',
    '案件类型:民事案件',
    '案件类型:行政案件',
    '案件类型:赔偿案件',
    '案件类型:执行案件'
    ]

for param in wenshu_index_params:
    for d in wenshu_index_iter(param,100):
        print type(d),d
