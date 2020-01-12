import requests



import time



import time
headers2= {
'Host': 'www.macau-slot.com',
'Connection': 'keep-alive',
'Content-Length': '52',
'Accept': 'text/plain, */*; q=0.01',
'Origin': 'https://www.macau-slot.com',
'X-Requested-With':'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Referer': 'https://www.macau-slot.com/content/soccer/coming_bet.html',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',

}

data = {
'request_data':'5f9e1a5b950c6686ceed5dbd7cb7f8b1bee26edfddc5f292c4c6348a79c83addfd005a2245767e2e94378292121e23e45a8280a4c574c1705811806fbdc20f828ed0104b0352a8a3c2953d3f6404d97a2893b84ed76995cc193cd208dccd452b02493c5f7d860b5a9602f101dd61ff9a3a1556856ca7ff8ffaeda09dc49b896b5fe66e63d9ec4a09723e71f8771620a69f323ab0344dc0c442d2806231eaedeea3383f32af2c9ff342382e10e95a08ada0cc24a57c5b2d54a6eb4c51910c3721',
'token': None
}

def post(url):
    r  = requests.Session()
    r.headers.update(headers2)
    rep=r.post(url,data=data,verify=False)
    print(rep.status_code)
    print(rep.text)



if __name__ == '__main__':

    url='https://www.macau-slot.com/API_SEV/cn/D/FB/markets/coming/all/threeinone'

    post(url)

