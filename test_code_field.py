#!/usr/bin/env python3.5
# coding=utf-8
import re
import shelve


def get_sw_version(part_info):
    part = re.match("^\d{4}\d{1,2}\d{1,2}[\s\S]*$", part_info)
    if part is not None:
        package_info = part.group()
        return package_info[package_info.index('_') + 1:package_info.index('-', package_info.index('-') + 1)]
    else:
        return False


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



def store_to_db(swList):
    import shelve
    with shelve.open("T311-H311_SW_Mapping") as db:
        for obj in swList:
            db[obj.sw_version] = obj
    print("Done!")

if __name__ == '__main__':
    ## Example 1 (Try to run it)
    # dict_link = {}
    # link_list = ['http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20220118.1_3110-rc5-37W/VW_HM/CNS3.0_37W-VW_HM-H311_RC5-MAIN-20220118.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20211123.1_9260-rc1-NAVIMAP-37W/zr3-navimap-CHN/CNS3.0_37W-zr3-navimap-CHN-C926_RC1-MAIN-20211123.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20220118.1_3110-rc5-37W/VW_HM_sec/CNS3.0_37W-VW_HM_sec-0311_RC5-MAIN-20220118.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20211123.1_9260-rc1-37W/zr3-navimap-CHN_sec/CNS3.0_37W-zr3-navimap-CHN_sec-0926_RC1-MAIN-20211123.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20220118.1_3110-rc5-37W/VW_TW/CNS3.0_37W-VW_TW-T311_RC5-MAIN-20220118.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20201127.2_9200-rc2-NAVIMAP-37W/zr3-navimap-TW/CNS3.0_37W-zr3-navimap-TW-T920_RC2-MAIN-20201127.2-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20220118.1_3110-rc5-37W/VW_TW_sec/CNS3.0_37W-VW_TW_sec-0311_RC5-MAIN-20220118.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20201127.2_9200-rc2-37W/zr3-navimap-TW_sec/CNS3.0_37W-zr3-navimap-TW_sec-0920_RC2-MAIN-20201127.2-REL.tgz']
    # for i in link_list:
    #     for j in i.split('/'):
    #         result = get_sw_version(j)
    #         if result is not False:
    #             dict_link[result] = i
    # print(dict_link)

    ## Example 2 (Try to run it)
    # sw1 = SW_Link('http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20220118.1_3110-rc5-37W/VW_HM/CNS3.0_37W-VW_HM-H311_RC5-MAIN-20220118.1-REL.tgz')
    # sw1.setSW_version()
    # print(sw1)

    ## Example 3 (Try to run it)
    # tempList = []
    # link_list = ['http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20220118.1_3110-rc5-37W/VW_HM/CNS3.0_37W-VW_HM-H311_RC5-MAIN-20220118.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20211123.1_9260-rc1-NAVIMAP-37W/zr3-navimap-CHN/CNS3.0_37W-zr3-navimap-CHN-C926_RC1-MAIN-20211123.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20220118.1_3110-rc5-37W/VW_HM_sec/CNS3.0_37W-VW_HM_sec-0311_RC5-MAIN-20220118.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20211123.1_9260-rc1-37W/zr3-navimap-CHN_sec/CNS3.0_37W-zr3-navimap-CHN_sec-0926_RC1-MAIN-20211123.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20220118.1_3110-rc5-37W/VW_TW/CNS3.0_37W-VW_TW-T311_RC5-MAIN-20220118.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/weekly_release/20201127.2_9200-rc2-NAVIMAP-37W/zr3-navimap-TW/CNS3.0_37W-zr3-navimap-TW-T920_RC2-MAIN-20201127.2-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20220118.1_3110-rc5-37W/VW_TW_sec/CNS3.0_37W-VW_TW_sec-0311_RC5-MAIN-20220118.1-REL.tgz', 'http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20201127.2_9200-rc2-37W/zr3-navimap-TW_sec/CNS3.0_37W-zr3-navimap-TW_sec-0920_RC2-MAIN-20201127.2-REL.tgz']
    # for i in range(len(link_list)):
    #     for j in link_list:
    #         i = SW_Link(j)
    #         i.setSW_version()
    #         tempList.append(i)
    # print(tempList)
    # store_to_db(tempList)

    # Example 4 (Try to run it)
    with shelve.open('T311-H311_SW_Mapping') as db:
        for key in db:
            # print('%-3s=>%s' % (key, db[key]))
            # print(db[key])
            print(db[key].link)



