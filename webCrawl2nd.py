#!/usr/bin/env python3.5
# coding=utf-8

import os  # Add the func to operate linux command.
import string


def otcoder(uncoded: str) -> str:
    import requests
    from bs4 import BeautifulSoup

    # dic_headers = {
    #     "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1"
    # }
    otcoder_url = "http://cnninvmjnkns02.joynext.com/otcoder/"
    dic_data = {
        "code": uncoded
    }
    resp = requests.post(otcoder_url, data=dic_data)
    soup = BeautifulSoup(resp.text, 'lxml')
    p_node = soup.find('p', class_='generated')
    # return p_node.get_text().strip()
    print(p_node)
    return p_node.get_text().strip()
    '4A016EA11B4A037DFB81789C6795A85B632DC8D8A523C5CAEEDE1C53B5AD9F113D180AB0542906023521FD66D4B61652BA127EAC9D81DC559B828E4B97C96155'


def check_input() -> bool:
    s = input('Please input the uncoded:')
    if s.lower() == 'exit':
        print("Exiting Now")
        return False
    elif len(s) != 128:
        print('-------------------------------------------------------------------\n')
        print('Please check the length of uncoded!!!!' + ' Then try again please!!!!')
        print('-------------------------------------------------------------------\n')
        return check_input()
    else:
        # print("s", s)
        return s


if __name__ == '__main__':
    # while True:
    #     s = input('Please input the uncoded:')
    #     if s.lower() == 'exit':
    #         break
    #     else:
    #         assert len(s) == 128, print('Please check the length of uncoded!!!!' + ' Then try again please!!!!')
    #         print('-----------One time code generated successfully as below-----------\n'+otcoder(s))
    #         os.system('echo ' + otcoder(s) + '| xclip')
    #         print('-------------------------------------------------------------------\n')
    #         continue

    while True:
        result = check_input()
        if result == False:
            break
        else:
            print("result", result)
            print('-----------One time code generated successfully as below-----------\n' + otcoder(result))
            os.system('echo ' + otcoder(result) + '| xclip')
            print('-------------------------------------------------------------------\n')
            continue

