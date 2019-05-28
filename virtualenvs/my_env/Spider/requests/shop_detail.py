# -*- coding: utf-8 -*-

import random,time,csv,sys,re
import requests
from pyquery import PyQuery as pq

def random_sleep_time():
    b = random.random()*10
    if  b > 5:
        a = random.random() + 2
    else:
        a = random.random() + 1
    time.sleep(a)

# 请求头
USER_AGENT_LIST = [
'Mozilla/5.0 (X11; U; UNICOS lcLinux; en-US) Gecko/20140730 (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
'Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
'Mozilla/5.0 (Windows; U; ; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
'Mozilla/5.0 (Windows; U; ; en-EN) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
'Mozilla/5.0 (X11; U; Linux; ru-RU) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: 802 025a17d)',
'Mozilla/5.0 (X11; U; Linux; fi-FI) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: 754 46b659a)',
'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
]

head = {
            'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0])  # 随机获取
        }

cookies ={
'_hc.v':'c325dea4-8c75-f263-a9ef-c9417beebbe9.1552275049',
'_lxsdk_cuid':'1696acd9880c8-0f45d89bb579f-38395f03-100200-1696acd9880c8',
'_lxsdk':'1696acd9880c8-0f45d89bb579f-38395f03-100200-1696acd9880c8',
'baidusearch_ab':'citybranch%3AA%3A1%7Cindex%3AA%3A1',
'switchcityflashtoast':'1',
'cityid':'2',
'default_ab':'citylist%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1',
's_ViewType':'10',
'aburl':'1',
'cityInfo':'%7B%22cityId%22%3A1%2C%22cityName%22%3A%22%E4%B8%8A%E6%B5%B7%22%2C%22provinceId%22%3A0%2C%22parentCityId%22%3A0%2C%22cityOrderId%22%3A0%2C%22isActiveCity%22%3Afalse%2C%22cityEnName%22%3A%22shanghai%22%2C%22cityPyName%22%3Anull%2C%22cityAreaCode%22%3Anull%2C%22cityAbbrCode%22%3Anull%2C%22isOverseasCity%22%3Afalse%2C%22isScenery%22%3Afalse%2C%22TuanGouFlag%22%3A0%2C%22cityLevel%22%3A0%2C%22appHotLevel%22%3A0%2C%22gLat%22%3A0%2C%22gLng%22%3A0%2C%22directURL%22%3Anull%2C%22standardEnName%22%3Anull%7D',
'__utma':'1.446456528.1552526029.1552526029.1552526029.1',
'__utmz':'1.1552526029.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
'_dp.ac.v':'97a73542-6a6c-4526-a925-0fdd87cf1751',
'cy':'1',
'cye':'shanghai',
'selectLevel':'%7B%22level1%22%3A%221%22%2C%22level2%22%3A%221%22%7D',
'_adwp':'169583271.4954857786.1552381290.1552381290.1552619045.2',
'Hm_lvt_dbeeb675516927da776beeb1d9802bd4':'1552381290,1552549460,1552619046',
'wedchatguest':'g-58078066719054151',
'ua':'dpuser_6063149380',
'ctu':'8972d2fd0f287d6f1e7677585dbf6c61af61a708250815608e78010a60399cfd',
'uamo':'18580936342',
'_lx_utm':'utm_source%3DBaidu%26utm_medium%3Dorganic',

'_lxsdk_s':'16994844abe-766-fae-d04%7C%7C60',
'dper':'53fd4c1ca3679cd72ca8437ed2e94c709b996950b1867d783d9b1f517b6defb78a12a9f238aa6a9474fff8336d3e4ea41748197c110617624ee5f95df26d59cc19feb7993d92f8fab6ce3e63caf041043ad266e6697fe0a27c1df2cab0f18275',
'll':'7fd06e815b796be3df069dec7836c3df',
}


#代理IP池
IPPOOL = [
    {'ipaddr': 'http://121.235.229.22:9999'}, {'ipaddr': 'http://142.234.201.107:80'},
    {'ipaddr': 'http://47.93.18.195:80'}, {'ipaddr': 'http://117.191.11.75:8080'},
    {'ipaddr': 'http://117.191.11.108:80'}, {'ipaddr': 'http://118.190.94.224:9001'},
    {'ipaddr': 'http://117.191.11.102:80'}, {'ipaddr': 'http://61.178.238.122:63000'},
    {'ipaddr': 'http://39.137.69.8:80'}, {'ipaddr': 'http://117.191.11.107:80'},
    {'ipaddr': 'http://39.137.168.229:8080'}, {'ipaddr': 'http://103.46.128.41:35033'},
    {'ipaddr': 'http://121.230.252.108:9999'}, {'ipaddr': 'http://125.40.238.181:56738'},
    {'ipaddr': 'http://221.180.204.144:80'}, {'ipaddr': 'http://223.68.190.130:8181'},
    {'ipaddr': 'http://118.190.95.43:9001'}, {'ipaddr': 'http://39.137.46.70:8080'},
    {'ipaddr': 'http://117.191.11.111:8080'}, {'ipaddr': 'http://120.210.219.74:8080'},
    {'ipaddr': 'http://106.14.77.200:80'}, {'ipaddr': 'http://39.137.46.73:80'},

]


#解析HTML代码
def geturl(page, data):
    print('start findurl')

# 抓取
def shoplistSpider(baseurl):
    print(baseurl)
    ban_bl = False
    cnt = 0
    while not ban_bl:
        cnt += 1
        proxies = random.sample(IPPOOL, 1)[0]  # 随机获取
        random_sleep_time()
        html = requests.get(baseurl, headers=head, proxies=proxies)
        print(html)
        pat = re.compile('.*' + '验证|无法访问' + '.*')
        ban_bl = pat.findall(html.text)
        print(ban_bl)
        print(bool(ban_bl))
        if not ban_bl:
            ban_bl = True
            print("200head:", head)
            print("200IP:", proxies)
            doc = pq(html.text)
            #图文混排
            pat1 = re.compile(r'<link rel="stylesheet" type="text/css" href="//s3plus'+ '.*' + '.css">')
            css_image = pat1.findall(html.text)
            print(css_image)
            #商户路径
            shop_addrs = doc('.breadcrumb').text().split()
            shop_title = pq(doc('#basic-info').html())
            # 商户星级
            shop_start = shop_title('.brief-info').children().attr('title')
            # 评论总是数
            comm_count = shop_title('#reviewCount').html()
            # 人均
            avgPriceTitle = shop_title('#avgPriceTitle').html()
            # 口味、环境、服务
            comment_score = shop_title('#comment_score').html()
            # 地址
            address = shop_title('span[id="address"]').html()
            # 电话
            tel_info = shop_title('p[class="expand-info tel"]').html()
            # 营业时间
            opentime = doc('p[class="info info-indent"]').children('.item').html()
            shop_head = {
                "shop_name：": shop_addrs[-1],
                "shop_start：": shop_start,
                "comment_cnt：": comm_count,
                "avg_price：": avgPriceTitle,
                "base_graded：": comment_score,
                "detail_addr：": address + '>>:' + str(shop_addrs),
                "tel_number：": tel_info,
                "open_time：": opentime,
            }

            shop_comment = pq(doc('#comment').html())
            # 评论比例
            cmt_ratio = shop_comment('div[class="comment-filter-box clearfix J-filter"]').text()
            cmt_dic = {"comment_ratio：": cmt_ratio}
            scls = [cmt_dic]

            for i in range(0, 10):

                html = shop_comment('ul[class="comment-list J-list"]').children().eq(i).html()
                doc_cd = pq(html)
                # 用户名
                cmt_user = doc_cd.children().eq(1).text()
                # 人均，有的没有
                average = doc_cd('span[class="average"]').text()
                # 评论内容前10
                cmt_detail = doc_cd('p[class="desc J-desc"]').html()
                if not cmt_detail:
                    cmt_detail = doc_cd('p[class="desc"]').html()
                doc_ls = {
                    "user_name：": cmt_user,
                    "avg_price：": average,
                    "comment_detail：": cmt_detail,
                }
                scls.append(doc_ls)
            print(shop_addrs)

            random_sleep_time()
            with open('shop_detail.csv', 'a', newline="", encoding='utf-8') as stf:
                # with open('shop_list.csv','ab') as stf:
                print("start save!!!")
                csv_stf = csv.writer(stf)
                shop_info = [baseurl, shop_head, scls, css_image]
                csv_stf.writerow(shop_info)
        else:
            if ban_bl and cnt < 10:
                ban_bl = False
                time.sleep(30)
                print(ban_bl)
                random_sleep_time()
            else:
                ban_bl = True
                print(ban_bl)

    # time.sleep(3)
    # random_sleep_time()

if __name__ == '__main__':
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    ssul = [
        # 'http://www.dianping.com/shop/96133575',
        # 'http://www.dianping.com/shop/3272494',
        # 'http://www.dianping.com/shop/90953185',
        # 'http://www.dianping.com/shop/23635682',
        # 'http://www.dianping.com/shop/14193579',
        # 'http://www.dianping.com/shop/114901521',
        # 'http://www.dianping.com/shop/93232872',
        # 'http://www.dianping.com/shop/127816792',
        # 'http://www.dianping.com/shop/113871220',
        # 'http://www.dianping.com/shop/5294362',
        # 'http://www.dianping.com/shop/16967298',
        # 'http://www.dianping.com/shop/67775427',
        # 'http://www.dianping.com/shop/24338223',
        'http://www.dianping.com/shop/122906254',
        'http://www.dianping.com/shop/110964474',
        # 'http://www.dianping.com/shop/4542549',
        # 'http://www.dianping.com/shop/22708171',
        # 'http://www.dianping.com/shop/6057527',
        # 'http://www.dianping.com/shop/6109691',
        # 'http://www.dianping.com/shop/127048021',
        # 'http://www.dianping.com/shop/2399464',
        # 'http://www.dianping.com/shop/68052206',
        # 'http://www.dianping.com/shop/102524307',
        # 'http://www.dianping.com/shop/98724378',

]
    for ssurl in ssul:
        shoplistSpider(ssurl)
        random_sleep_time()