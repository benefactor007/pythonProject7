#!/usr/bin/env python3.5

"""
scp -r -v  `ls |grep -v 1|xargs` /home/jpcc/Downloads/temp2/
Note: copy except what don't want by using 'ls | grep -v *|xargs'
"""


if __name__ == '__main__':

    import requests
    # import json
    from bs4 import BeautifulSoup


    dic_headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1 "
    }

    # url = 'http://cnninvmjnkns02.joynext.com/otcoder/'
    # url = 'http://cnninvmcnflnc01:8090/pages/viewpage.action'
    url = 'http://cnninvmcnflnc01:8090/pages/viewpage.action?pageId=82597775'
    param = {
        "pageId" : "82597775"
    }
    # resp = requests.get(url = url, params=param, headers = dic_headers)
    resp = requests.get(url=url, headers=dic_headers)
    # resp = requests.get(url=url, params=param)
    # print(resp.request.url)
    # print(resp.text.strip())
    # soup = BeautifulSoup(resp.text, 'lxml')
    # print(soup.find_all())
    print(resp.text)

