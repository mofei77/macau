
data  = 'data: c.genData(e, h)'

next_page  = 'gotoNumberPage'
event=  'markets/coming/all'

event_it = 'event_insert_'
import execjs

js = """
var i=100

!function(){ i =200}()
function run(){
   
    return i
}
"""
r_data = {'request_data':'923e8a67fa6065b915eadce6a9ed7e4f1f8e0f581a07d479bf6b6f2841c198f807ec091987852e27cf24f3c51e491231471f943280e4b43b17da2538691e7d2d2a23f5aa696bee1464b8f56da25152e05ba8a830bcbe458348c101b6043611412029c76a70de04f49b0ab2b4814b056a2b625524591b4154541bb6c1944188aae2a4b85bcd3be2f7a51eca42c17ba04e2b65e5c0aa79c4add3b75569b63a7add1914cfc66683abfbe4a38d72604839230149236a68a3c7d78aa648ff0988e38b',
            'token':''
          }
import requests
head = {
'Host': 'www.macau-slot.com',
'Connection': 'keep-alive',
'Content-Length': '340',
'Accept': 'text/plain, */*; q=0.01',
'Origin': 'https://www.macau-slot.com',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Referer':'https://www.macau-slot.com/content/soccer/coming_bet.html',

'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
#'Cookie': '_ga=GA1.2.135589650.1578579797; _gid=GA1.2.333006610.1578579797; isOpenWindow=true; Hm_lvt_985cfcc018e331d22092d9275e258d69=1578763971,1578768698,1578770265,1578805502; Hm_lpvt_985cfcc018e331d22092d9275e258d69=1578805502; JSESSIONID=LwZB1BVQmfn5THZeN7-ciW1HptiTkMfigidiC6_Z; _gat=1; AWSALB=z7V6ZQZeFGTCQRAcE59RZrcgQDOB8M0JPy5YqH7Ky54Wf8GnoUsoRPW+QFV1oGEwV5k+HJDTvpBhK/6k4hWqt6x8tZwVhPKJ6Sl+yaYaFSKHDYcZJgsg6o/NSmzJ'


}
url = 'https://www.macau-slot.com/API_SEV/cn/D/FB/markets/coming/all/cs'
sess = requests.session()
sess.headers.update(head)
r = sess.post(url,data=r_data)
print(r.content)
print(r.cookies)