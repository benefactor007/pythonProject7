# install requests
# pip install requests
# Requirement already satisfied: requests in /usr/lib/python3/dist-packages (2.9.1)
# The 2nd way: download from the chinese open source.
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simpl requests
# https://mirrors.tuna.tsinghua.edu.cn/help/pypi/


if __name__ == '__main__':
    import requests
    # import json
    from bs4 import BeautifulSoup

    # dic_headers = {
    #     "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1"
    # }
    #
    # url = 'http://cnninvmjnkns02.joynext.com/otcoder/'
    # resp = requests.get(url, headers = dic_headers)
    #
    # print(resp)                   # Output: <Response [200]>
    # print(resp.request)           # Output: <PreparedRequest [GET]>
    # print(resp.text)              # Output: source code

    url = "http://cnninvmjnkns02.joynext.com/otcoder/"

    # s = input("Please input the uncoded:")

    """
    4A016EA11B4A037DFB81789C6795A85B632DC8D8A523C5CAEEDE1C53B5AD9F113D180AB0542906023521FD66D4B61652BA127EAC9D81DC559B828E4B97C96155
    """

    dic_data = {
        "code": "4A016EA11B4A037DFB81789C6795A85B632DC8D8A523C5CAEEDE1C53B5AD9F113D180AB0542906023521FD66D4B61652BA127EAC9D81DC559B828E4B97C96155"
    }

    # Submit the post request
    resp = requests.post(url, data=dic_data)
    # print(resp.text)
    # json.loads(resp)                          # Output: Error
    # print(resp.json())                        # Output: Error
    soup = BeautifulSoup(resp.text, 'lxml')
    # print(soup.prettify())
    # print(soup.p.parent)
    p_node = soup.find('p', class_='generated')
    print(p_node.get_text().strip())
