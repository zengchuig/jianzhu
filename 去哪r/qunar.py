from settings import *
import requests,re,os

u1='https://flight.qunar.com/touch/api/domestic/wbdflightlist'
u2='https://flight.qunar.com/site/oneway_list.htm'
headers2={'cookie':'QN1=00001680306822dc2c6854b1; QN300=flight.qunar.com; QN99=1886; _i=ueHd8LJIfk-XHfxXUaRNjx30k40X; QN170=113.246.227.198_4f4bb9_0_8UeSfoPmyeEaGWojaaoJXUak3G%2BhFERymzDnUl2b2Dc%3D; fid=18ecb0c3-27db-4204-b73e-6e8c9aba340a; QN48=e86d2a95-4a5b-4004-b4a5-0672111ad242; F234=1587871633712; F235=1587871633712; QunarGlobal=10.95.13.37_-25cb3614_171a65fad80_-2665%7C1587871633782; QN621=1490067914133%3DDEFAULT; QN66=qunar; QN667=C; QN668=51%2C55%2C58%2C57%2C58%2C57%2C51%2C57%2C55%2C58%2C56%2C59%2C59',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
'referer':'https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E9%95%BF%E6%B2%99&searchArrivalAirport=%E4%B8%8A%E6%B5%B7&searchDepartureTime=2020-04-30&searchArrivalTime=2020-05-01&nextNDays=0&startSearch=true&fromCode=CSX&toCode=SHA&from=flight_dom_search&lowestPrice=null',
}

params={
    'departureCity': '长沙',
    'arrivalCity': '上海',
    'departureDate': departureDate,
    'ex_track': '',
    '__m__': '8e0a724f67365da35da21b39b96fa91d',
    'st': '1587877803909',
    'sort': '',
    '_v': '4',
}
params2={
    'searchDepartureAirport': '长沙',
    'searchArrivalAirport': '上海',
    'searchDepartureTime': departureDate,
    'searchArrivalTime': '2020-05-01',
    'nextNDays': '0',
    'startSearch': 'true',
    'fromCode': 'CSX',
    'toCode': 'SHA',
    'from': 'flight_dom_search',
    'lowestPrice': 'null',
}

def get_pre():
    resp=requests.get(u2,headers=headers2,params=params2).text
    l2=re.search('<script>(var.*?)</script>',resp).group(1)
    value1=re.search('\}window.*?=(.*?);',l2).group(1)
    print(value1)
    value2=re.search('var '+value1+'.*?;',l2).group()
    print(value2)
    l2=l2.replace(value2,value2+'console.log('+value1+');')
    l2=re.sub(value2,value2+'console.log('+value1+');',l2)
    with open('pre.js','w') as f:
        f.write(l1+'\n'+l2)
    pre=os.popen('node pre.js').read()
    return pre

pre=get_pre().strip()
print(pre)
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
          'cookie':'QN269=DE860140877C11EAAAB4FA163E8E8E85;csrfToken=w94joDoxb1N7JaRhFz2rSZdDLoqx5lAy;QN267=070860963578feb675;Alina=87c5cfa0-01db76-93414b59-39b2a541-1cc25ea517ac;QN271=442f8515-7a78-45bf-b828-3b6013ef44a5;QN1=00001680306822dc2c6854b1; QN300=flight.qunar.com; QN99=1886; QN601=01f4e2b6e73a7a2e5b63126c17922a2e; _i=ueHd8LJIfk-XHfxXUaRNjx30k40X; _vi=nFI_AqK5igxD1KXxqn7VXTwDQmZmWUSbsioBh4mit6eqEfgT4kYS4lDNH6qdpq6N6YbA7RKCaGUc2ijTIjBpyCAEfIVtvU-2q4ndPnl2OCKUWSPMKHy5A17ir3NAZDfMovqlfyRiwt_SwCBwXu7ydEqVjIlSvMoUty1yOaeo2btI; QN170=113.246.227.198_4f4bb9_0_8UeSfoPmyeEaGWojaaoJXUak3G%2BhFERymzDnUl2b2Dc%3D; fid=18ecb0c3-27db-4204-b73e-6e8c9aba340a; QN48=e86d2a95-4a5b-4004-b4a5-0672111ad242; F234=1587871633712; F235=1587871633712; QunarGlobal=10.95.13.37_-25cb3614_171a65fad80_-2665%7C1587871633782; SC1=364d6484c8b099ad1124df526a9989ab; SC18=; QN621=1490067914133%3DDEFAULT; QN66=qunar; QN667=A; QN668=51%2C55%2C58%2C57%2C58%2C57%2C51%2C58%2C51%2C55%2C59%2C51%2C55',
          'csht':'',
          'pre':pre,
          'w':'0',
          'referer':'https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E9%95%BF%E6%B2%99&searchArrivalAirport=%E4%B8%8A%E6%B5%B7&searchDepartureTime=2020-04-30&searchArrivalTime=2020-05-01&nextNDays=0&startSearch=true&fromCode=CSX&toCode=SHA&from=flight_dom_search&lowestPrice=null',
          'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
}
print(headers)
resp=requests.get(u1,headers=headers,params=params)
with open('caogao','w') as f:
    f.write(resp.text)

# -----------------以下是部分cookies，前期摸索时所写，很操蛋----------------------
# 这是_i,_vi,由服务器返回
# se=requests.session()
# u_vi='https://user.qunar.com/passport/addICK.jsp?ssl'
# resp=se.get(u_vi,headers=headers2)
# q=se.cookies
# print(q,resp.url)

# 这是QN_271,等于服务器返回的SessionId
# u_sess='https://rmcsdf.qunar.com/js/df.js?org_id=ucenter.login&js_type=0'
# resp=requests.get(u_sess,headers=headers2).text
# print(resp)

# 这是QN_269
# u_269='https://s.c-ctrip.com/universal-id.js?callback=_qheader_ctrip_callcallback'
# resp=requests.get(u_269,headers=headers2).text
# print(resp)
