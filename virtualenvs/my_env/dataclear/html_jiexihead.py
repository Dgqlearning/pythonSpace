# -!- coding: utf-8 -!-
import json
from pyquery import PyQuery as PQ
import ast
import csv, re
from lxml import etree
from xml.etree.ElementTree import parse
from itertools import chain




html = ''
with open('ONL49900007A1.508','r', encoding='gb18030',errors="ignore") as stf:
    print("start jiexi!!!")
    html = stf.read()

pat1 = re.compile('<CFX>.*?</CFX>')
html = pat1.findall(html)
cnt = 0
maxa = []
for i in html[0:]:
    cnt += 1
    print(cnt)
    i = r'<?xml version="1.0"?>' + i
    # ~ 将html转换成_Element对象
    _element = etree.XML(i)
    with open('catesareas.csv','a',newline="", encoding='utf-8') as stf:
        print("start save!!!")
        csv_stfs = csv.writer(stf)
        xmlt = list(_element.iter())
        tags = []
        for i in xmlt:
            tags.append(i.tag)
        st_tag = set(tags)    
        print(len(st_tag))
        maxa.append(len(st_tag))    
            # ~ rowk = [x+'\t' for x in rowk]
            # ~ csv_stfs.writerow(rowk) 
        
print('>>max>>>',max(maxa), maxa.index(max(maxa)))            
