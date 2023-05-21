import requests
import re


def get_tel(id):
    cookies = {
        'Article%5FID': id,
        'ASPSESSIONIDAUCRRDTA': 'ICBDHDJACGMBBGCFAPOGALII',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'Article%5FID=6623; ASPSESSIONIDAUCRRDTA=ICBDHDJACGMBBGCFAPOGALII',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'ID': id,
    }

    response = requests.get('https://www.zmuhospital.com/M/Show.asp', params=params, cookies=cookies, headers=headers)
    patter = "(?<!\d)(1\d{10})(?!\d)"
    res_phone = re.compile(patter).findall(response.text)
    if len(res_phone) != 0:
        print(res_phone)


def get_tel1(id):
    import requests

    cookies = {
        'Article%5FKeyword': '%D7%F1%D2%BD%B8%BD%D4%BA',
        'Article%5FID': id,
        'Hm_lvt_283a5e8e4ccbf6354656deac91f1b050': '1684673440',
        'Hm_lpvt_283a5e8e4ccbf6354656deac91f1b050': '1684673440',
        'CP': 'OK',
        'ASPSESSIONIDAUCRRDTA': 'HNDDHDJAGOHCBCHNDHFOFKKB',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'Article%5FKeyword=%D7%F1%D2%BD%B8%BD%D4%BA; Article%5FID=2552; Hm_lvt_283a5e8e4ccbf6354656deac91f1b050=1684673440; Hm_lpvt_283a5e8e4ccbf6354656deac91f1b050=1684673440; CP=OK; ASPSESSIONIDAUCRRDTA=HNDDHDJAGOHCBCHNDHFOFKKB',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'id': id,
    }

    response = requests.get('https://www.zmuhospital.com/Article/Show.asp', params=params, cookies=cookies,
                            headers=headers)
    patter = "(?<!\d)(1\d{10})(?!\d)"
    res_phone = re.compile(patter).findall(response.text)
    if len(res_phone) != 0:
        print(res_phone)


def get_tel2(id):
    import requests

    cookies = {
        'Hm_lvt_283a5e8e4ccbf6354656deac91f1b050': '1684673440',
        'Article%5FID': id,
        'Article%5FKeyword': '%D5%D0%B1%EA',
        'ASPSESSIONIDAUCRRDTA': 'OJEDHDJAFMLDKEMCHKACJBOM',
        'Hm_lpvt_283a5e8e4ccbf6354656deac91f1b050': '1684673654',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'Hm_lvt_283a5e8e4ccbf6354656deac91f1b050=1684673440; Article%5FID=17491; Article%5FKeyword=%D5%D0%B1%EA; ASPSESSIONIDAUCRRDTA=OJEDHDJAFMLDKEMCHKACJBOM; Hm_lpvt_283a5e8e4ccbf6354656deac91f1b050=1684673654',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://www.zmuhospital.com/Article/' + str(id) + '.html', cookies=cookies,
                            headers=headers)

    patter = "(?<!\d)(1\d{10})(?!\d)"
    res_phone = re.compile(patter).findall(response.text)
    if len(res_phone) != 0:
        print(res_phone)


for i in range(1, 7000):
    get_tel(i)
    get_tel1(i)
    get_tel2(i)
