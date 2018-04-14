# coding='utf-8'
import dfslogging
import requests
import os.path
from bs4 import BeautifulSoup

dfs_header_first = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
                    'Connection': 'keep-alive',
                    'Host': 'www.taobao.com',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
                    }


dfs_header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
              'Connection': 'keep-alive',
              'Host': 'login.taobao.com',
              'Referer': 'https://www.taobao.com',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
              }
taobao_base_url = 'https://www.taobao.com'
taobao_login_url = 'https://login.taobao.com/member/login.jhtml'
if __name__ == '__main__':
    # begining of the app
    dfslogging.logger.info('start app')

    s = requests.Session()
    # s.verify = False
    # s.verify = r'dofospider1.cer'
    # s.cert = r'dofospider1.cer'

    res = s.get(taobao_base_url, headers=dfs_header_first)
    # dfslogging.logger.info(res)
    # dfslogging.logger.info(res.cookies)
    # dfslogging.logger.info(type(res.cookies))
    # dfslogging.logger.info(dir(res.cookies))
    # dfslogging.logger.info(res.cookies.items)

    log = s.get(taobao_login_url, headers=dfs_header)
    dfslogging.logger.info(log.text)
    # geturl = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.\ train_date=2017-04-29&leftTicketDTO.from_station=WHN&leftTicketDTO.\ to_station=SZN&purpose_codes=ADULT"
    # 测试网址
    # # geturl = "http://blog.csdn.net/wangming520liwei/article/details/53896964"
    # res = requests.get(geturl,headers=my_header)
    # res = requests.get(geturl, headers=my_header, verify=False)
    # res = requests.get(geturl,headers=my_header,verify="E:/SRCA.crt")
    # res.encoding = 'utf-8'
    # soup = BeautifulSoup(res.text, 'html5lib')

    # ending of the app
    dfslogging.logger.info('end app')
