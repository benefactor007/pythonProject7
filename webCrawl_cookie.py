#!/usr/bin/env python3.5
# coding=utf-8
import re

import requests
import json

from bs4 import BeautifulSoup


class AttrDisplay:
    """
    Provides an inheritable(inˈherədəb(ə)l) display overload method that shows instance with their class
    names and a name=value pair for each attribute stored on the instance itself (but not attrs inherited from its
    class). Can be mixed into any class, and will work on any instance
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%+3s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


class SW_Link(AttrDisplay):
    def __init__(self, link, sw_version = None):
        self.link = link
        self.sw_version = sw_version
    def setSW_version(self):
        for i in self.link.split('/'):
            part = re.match("^\d{4}\d{1,2}\d{1,2}[\s\S]*$", i)
            if part is not None:
                package_info = part.group()
                self.sw_version = package_info[package_info.index('_') + 1:package_info.index('-', package_info.index('-') + 1)]

# -------------------------Don't not delete the content as follows-----------------------------------------------------
if __name__ == '__main__':
    # conversation
    session = requests.session()
    data = {
            "os_username": "wu_j7",
            "os_password": "Tianyuan==xu",
            "login": "Log+in",
            "os_destination": ""
    }
    dic_headers = {
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            # "Accept-Encoding": "gzip, deflate",
            # "Accept-Language": "en-US,en;q=0.5",
            # "Connection": "keep-alive",
            # "Content-Length": "75",
            # "Content-Type": "application/x-www-form-urlencoded",
            # "Host": "cnninvmcnflnc01:8090",
            # "Origin": "http://cnninvmcnflnc01:8090",
            # "Referer": "http://cnninvmcnflnc01:8090/login.action?logout=true",
            # "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }

    # ajs-remote-user
    print(data)
    url_login = "http://cnninvmcnflnc01:8090/login.action"
    session.post(url=url_login, data=data, headers=dic_headers)
    # url_SWRTPL = "http://cnninvmcnflnc01:8090/pages/viewpage.action"
    url_SWRTPL = input("Please input the Confluence page address (Software release to production line):")
    # url_SWRTPL = "http://cnninvmcnflnc01:8090/display/PCNSSOP2/C665+SW+Mapping"
    # param = {
    #     "pageId": "82597775"
    # }
    # resp = session.get(url=url_SWRTPL,params=param)
    resp = session.get(url=url_SWRTPL)
    # print(resp.text)

    soup = BeautifulSoup(resp.text, 'lxml')
    """
            <p>In general,</p><p>1. TW software should use TW MAP, for other variant CHN MAP should be used.</p><p>2. CHN MAP data can't be provided to location that out of Chinese Mainland.</p><p>3. SEC software should be used on CK HW.</p><p><br/></p><div class="table-wrap"><table class="relative-table wrapped confluenceTable"><colgroup><col style="width: 121.0px;"/><col style="width: 111.0px;"/><col style="width: 79.0px;"/><col style="width: 149.0px;"/><col style="width: 102.0px;"/><col style="width: 84.0px;"/><col style="width: 85.0px;"/><col style="width: 221.0px;"/><col style="width: 85.0px;"/><col style="width: 221.0px;"/><col style="width: 173.0px;"/></colgroup><tbody><tr><td style="text-align: center;" class="confluenceTd"><p><strong>Customer PN</strong></p></td><td style="text-align: center;" class="confluenceTd"><p><strong>Variant</strong></p></td><td style="text-align: center;" colspan="1" class="confluenceTd"><strong>Brand</strong></td><td style="text-align: center;" colspan="1" class="confluenceTd"><strong>Market</strong></td><td style="text-align: center;" colspan="1" class="confluenceTd"><strong>Produced by</strong></td><td style="text-align: center;" colspan="1" class="confluenceTd"><strong>SW Variant</strong></td><td colspan="1" class="confluenceTd"><strong>SW Version</strong></td><td colspan="1" class="confluenceTd"><strong>SW Link</strong></td><td colspan="1" class="confluenceTd"><strong>MAP Version</strong></td><td colspan="1" class="confluenceTd"><strong>MAP Link</strong></td><td colspan="1" class="confluenceTd"><p><strong>E-Signature</strong></p><p><strong>(Check Result)</strong></p></td></tr><tr><td rowspan="4" class="confluenceTd"><p align="center">5HG.035.866</p></td><td class="confluenceTd"><p>SVW_CN DK C0</p></td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">Chinese Mainland</td><td colspan="1" class="confluenceTd">SVW</td><td colspan="1" class="confluenceTd">VW CHN</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td></tr><tr><td class="confluenceTd"><p>SVW_CN CK C0</p></td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">Chinese Mainland</td><td colspan="1" class="confluenceTd">SVW</td><td colspan="1" class="confluenceTd">VW CHN SEC</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td></tr><tr><td class="confluenceTd"><p>FAW-VW_CN DK C0</p></td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">Chinese Mainland</td><td colspan="1" class="confluenceTd">FAW-VW</td><td colspan="1" class="confluenceTd">VW CHN</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td></tr><tr><td class="confluenceTd"><p>FAW-VW_CN CK C0</p></td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">Chinese Mainland</td><td colspan="1" class="confluenceTd">FAW-VW</td><td colspan="1" class="confluenceTd">VW CHN SEC</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td><td colspan="1" class="confluenceTd"><br/></td></tr><tr><td rowspan="2" class="confluenceTd"><p align="center">5DD.035.866</p></td><td class="confluenceTd"><p>SK_CN DK C0</p></td><td colspan="1" class="confluenceTd">SKODA</td><td colspan="1" class="confluenceTd">Chinese Mainland</td><td colspan="1" class="confluenceTd">SKODA</td><td colspan="1" class="confluenceTd">SK CHN</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td></tr><tr><td class="confluenceTd"><p>SK_CN CK C0</p></td><td colspan="1" class="confluenceTd">SKODA</td><td colspan="1" class="confluenceTd">Chinese Mainland</td><td colspan="1" class="confluenceTd">SKODA</td><td colspan="1" class="confluenceTd">SK CHN SEC</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td></tr><tr><td rowspan="2" class="confluenceTd"><p align="center">5HG.035.864</p></td><td class="confluenceTd"><p>VW_HM DK C0</p></td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">HongKong/MAC</td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">VW HM</td><td colspan="1" class="confluenceTd">H311</td><td colspan="1" class="confluenceTd"><a href="http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20220118.1_3110-rc5-37W/VW_HM/CNS3.0_37W-VW_HM-H311_RC5-MAIN-20220118.1-REL.tgz" class="external-link" rel="nofollow">http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20220118.1_3110-rc5-37W/VW_HM/CNS3.0_37W-VW_HM-H311_RC5-MAIN-20220118.1-REL.tgz</a></td><td colspan="1" class="confluenceTd">9260</td><td colspan="1" class="confluenceTd"><a href="http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20211123.1_9260-rc1-NAVIMAP-37W/zr3-navimap-CHN/CNS3.0_37W-zr3-navimap-CHN-C926_RC1-MAIN-20211123.1-REL.tgz" class="external-link" rel="nofollow">http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20211123.1_9260-rc1-NAVIMAP-37W/zr3-navimap-CHN/CNS3.0_37W-zr3-navimap-CHN-C926_RC1-MAIN-20211123.1-REL.tgz</a></td><td colspan="1" class="confluenceTd"><div class="content-wrapper"><ul class="inline-task-list" data-inline-tasks-content-id="82597775"><li class="checked" data-inline-task-id="1">PM: <a class="confluence-userlink user-mention" data-username="chen_c3" href="/display/~chen_c3" data-linked-resource-id="6455299" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="http://cnninvmcnflnc01.joynext.com:8090">Chen Chao</a></li><li class="checked" data-inline-task-id="2">TPM: <br/><a class="confluence-userlink user-mention" data-username="zhang_q7" href="/display/~zhang_q7" data-linked-resource-id="74485973" data-linked-resource-version="2" data-linked-resource-type="userinfo" data-base-url="http://cnninvmcnflnc01.joynext.com:8090">Zhang Qiang2</a></li></ul></div></td></tr><tr><td class="confluenceTd"><p>VW_HM CK C0</p></td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">HongKong/MAC</td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">VW HM SEC</td><td colspan="1" class="confluenceTd">0311</td><td colspan="1" class="confluenceTd"><a href="http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20220118.1_3110-rc5-37W/VW_HM_sec/CNS3.0_37W-VW_HM_sec-0311_RC5-MAIN-20220118.1-REL.tgz" class="external-link" rel="nofollow">http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20220118.1_3110-rc5-37W/VW_HM_sec/CNS3.0_37W-VW_HM_sec-0311_RC5-MAIN-20220118.1-REL.tgz</a></td><td colspan="1" class="confluenceTd">9260</td><td colspan="1" class="confluenceTd"><a href="http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20211123.1_9260-rc1-37W/zr3-navimap-CHN_sec/CNS3.0_37W-zr3-navimap-CHN_sec-0926_RC1-MAIN-20211123.1-REL.tgz" class="external-link" rel="nofollow">http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20211123.1_9260-rc1-37W/zr3-navimap-CHN_sec/CNS3.0_37W-zr3-navimap-CHN_sec-0926_RC1-MAIN-20211123.1-REL.tgz</a></td><td colspan="1" class="confluenceTd"><div class="content-wrapper"><ul class="inline-task-list" data-inline-tasks-content-id="82597775"><li class="checked" data-inline-task-id="0">PM: <a class="confluence-userlink user-mention" data-username="chen_c3" href="/display/~chen_c3" data-linked-resource-id="6455299" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="http://cnninvmcnflnc01.joynext.com:8090">Chen Chao</a></li><li class="checked" data-inline-task-id="8">TPM: <br/><a class="confluence-userlink user-mention" data-username="zhang_q7" href="/display/~zhang_q7" data-linked-resource-id="74485973" data-linked-resource-version="2" data-linked-resource-type="userinfo" data-base-url="http://cnninvmcnflnc01.joynext.com:8090">Zhang Qiang2</a></li></ul></div></td></tr><tr><td rowspan="2" class="confluenceTd"><p align="center">5HG.035.877</p></td><td class="confluenceTd"><p>VW_TW DK C0</p></td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">TWN</td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd"><p>VW TW</p></td><td colspan="1" class="confluenceTd">T311</td><td colspan="1" class="confluenceTd"><a href="http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20220118.1_3110-rc5-37W/VW_TW/CNS3.0_37W-VW_TW-T311_RC5-MAIN-20220118.1-REL.tgz" class="external-link" rel="nofollow">http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20220118.1_3110-rc5-37W/VW_TW/CNS3.0_37W-VW_TW-T311_RC5-MAIN-20220118.1-REL.tgz</a></td><td colspan="1" class="confluenceTd">9200</td><td colspan="1" class="confluenceTd"><a rel="nofollow" href="http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20201127.2_9200-rc2-NAVIMAP-37W/zr3-navimap-TW/CNS3.0_37W-zr3-navimap-TW-T920_RC2-MAIN-20201127.2-REL.tgz" class="external-link">http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20201127.2_9200-rc2-NAVIMAP-37W/zr3-navimap-TW/CNS3.0_37W-zr3-navimap-TW-T920_RC2-MAIN-20201127.2-REL.tgz</a></td><td colspan="1" class="confluenceTd"><div class="content-wrapper"><ul class="inline-task-list" data-inline-tasks-content-id="82597775"><li class="checked" data-inline-task-id="9">PM: <a class="confluence-userlink user-mention" data-username="chen_c3" href="/display/~chen_c3" data-linked-resource-id="6455299" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="http://cnninvmcnflnc01.joynext.com:8090">Chen Chao</a></li><li class="checked" data-inline-task-id="10">TPM: <br/><a class="confluence-userlink user-mention" data-username="zhang_q7" href="/display/~zhang_q7" data-linked-resource-id="74485973" data-linked-resource-version="2" data-linked-resource-type="userinfo" data-base-url="http://cnninvmcnflnc01.joynext.com:8090">Zhang Qiang2</a></li></ul></div></td></tr><tr><td class="confluenceTd"><p>VW_TW CK C0</p></td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd">TWN</td><td colspan="1" class="confluenceTd">VW</td><td colspan="1" class="confluenceTd"><p>VW TW SEC</p></td><td colspan="1" class="confluenceTd">0311</td><td colspan="1" class="confluenceTd"><a href="http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20220118.1_3110-rc5-37W/VW_TW_sec/CNS3.0_37W-VW_TW_sec-0311_RC5-MAIN-20220118.1-REL.tgz" class="external-link" rel="nofollow">http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20220118.1_3110-rc5-37W/VW_TW_sec/CNS3.0_37W-VW_TW_sec-0311_RC5-MAIN-20220118.1-REL.tgz</a></td><td colspan="1" class="confluenceTd">9200</td><td colspan="1" class="confluenceTd"><a href="http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20201127.2_9200-rc2-37W/zr3-navimap-TW_sec/CNS3.0_37W-zr3-navimap-TW_sec-0920_RC2-MAIN-20201127.2-REL.tgz" rel="nofollow" class="external-link">http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20201127.2_9200-rc2-37W/zr3-navimap-TW_sec/CNS3.0_37W-zr3-navimap-TW_sec-0920_RC2-MAIN-20201127.2-REL.tgz</a></td><td colspan="1" class="confluenceTd"><div class="content-wrapper"><ul class="inline-task-list" data-inline-tasks-content-id="82597775"><li class="checked" data-inline-task-id="11">PM: <a class="confluence-userlink user-mention" data-username="chen_c3" href="/display/~chen_c3" data-linked-resource-id="6455299" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="http://cnninvmcnflnc01.joynext.com:8090">Chen Chao</a></li><li class="checked" data-inline-task-id="12">TPM: <br/><a class="confluence-userlink user-mention" data-username="zhang_q7" href="/display/~zhang_q7" data-linked-resource-id="74485973" data-linked-resource-version="2" data-linked-resource-type="userinfo" data-base-url="http://cnninvmcnflnc01.joynext.com:8090">Zhang Qiang2</a></li></ul></div></td></tr><tr><td rowspan="2" class="confluenceTd"><p align="center">5DD.035.877</p></td><td class="confluenceTd"><p>SK_TW DK C0</p></td><td colspan="1" class="confluenceTd">SKODA</td><td colspan="1" class="confluenceTd">TWN</td><td colspan="1" class="confluenceTd">SKODA</td><td colspan="1" class="confluenceTd">SK TW</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td></tr><tr><td class="confluenceTd"><p>SK_TW CK C0</p></td><td colspan="1" class="confluenceTd">SKODA</td><td colspan="1" class="confluenceTd">TWN</td><td colspan="1" class="confluenceTd">SKODA</td><td colspan="1" class="confluenceTd">SK TW SEC</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td><td colspan="1" class="confluenceTd">-</td></tr></tbody></table></div>

    """
    swlinklist = []
    for x in soup.find_all('a', class_="external-link"):
        # print(x)
        link = x.get('href')
        if link:
            swlinklist.append(link)
    session.close()    # IMPORTANT: Need to close the session or request.
    # print(swlinklist)
    dict_sw = dict.fromkeys(swlinklist)
    print(dict_sw)
    for key in dict_sw.keys():
        print(key)
# -------------------------Don't not delete the content as above-------------------------------------------------------



