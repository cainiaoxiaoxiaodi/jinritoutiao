import json
import time

import execjs
import requests

for xyz in range(5):
    f = open(r"./_signature.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    ctx = execjs.compile(htmlstr)
    js = json.loads(ctx.call('get_as_cp_signature'))

    t =str(int(time.time()))
    url3 = 'https://m.toutiao.com/list/?tag=news_tech&ac=wap&count=20&format=json_raw&as='+str(js['as'])+'&cp='+str(js['cp'])+'&max_behot_time=' +str(js['_signature']) + '&_signature=C9XSbQAAUH.uYxbcBp2EywvV0n&i=' + t
    print(url3)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=165c0e9eccf644-019c6f854c259d-671c1574-144000-165c0e9ecd0655; tt_webid=6599388515396535822; uuid="w:dda5561d46e44f9a84f9ffe29719b7d9"; csrftoken=b1a225efceb3e3ab1eef1096d2162245; W2atIF=1; _ba=BA0.2-20180927-51225-1gKY9W2z0XrY03F4USJ9; _ga=GA1.2.1471916770.1538045297; utm_source=toutiao; _gid=GA1.2.1891596419.1538190941',
        'Host': 'm.toutiao.com',
        'Referer': 'https://m.toutiao.com/?channel=__all__',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    # try:
    response = requests.get(url3, headers=headers)
    print(response)
    # pprint(json.loads(response.content.decode()))
    js_list = json.loads(response.content.decode())['data']
    for js in js_list:
        with open('1.txt', 'a+', encoding='utf-8') as f:
            f.write(str(js)+'\n')
    # except:
    #     pass

    time.sleep(8)
