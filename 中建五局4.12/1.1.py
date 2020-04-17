from pymysql import connect
conn=connect(host='localhost',port=3306,user='root',password='222',database='qy_detail',charset='utf8')
cs=conn.cursor()
import requests,time,PyV8,json
url='http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?complexname=中建五局土木工程有限公司&pg=0&pgsz=15&total=0'
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        }
se=requests.session()
ctxt = PyV8.JSContext()
ctxt.enter()
f=open('jiemi.text')
k=f.read()
f.close()
func=ctxt.eval(k)

def set(callback):
    def call(url):
        i=0
        while True:
            resp=callback(url)
            if 'html' in resp.headers['Content-Type']:
                i+=1
                print('i=',i)
                time.sleep(1)
                if i>2:
                    raise err
            else:
                break
        return resp.text
    return call

@set
def resp1(url):
    resp=se.get(url,headers=headers)
    return resp

def date(timestamp):
    timeArray = time.localtime(timestamp/1000)
    date = time.strftime("%Y-%m-%d", timeArray)
    return date

def parse(ret,qy=None,total=None,zhuce=None,xiangmu=None):
    if qy:
        ret=func(ret)
        ret=json.loads(ret)
        data=ret['data']['list'][0]
        qy_name,region_name,org_code,qy_id,fr_name,collect_time=(data['QY_NAME'],data['QY_REGION_NAME'],
           data['QY_ORG_CODE'] ,data['QY_ID'],data['QY_FR_NAME'],data['COLLECT_TIME']
        )
        collect_time=date(collect_time)
        cs.execute("insert into qy values(0,'{}','{}','{}','{}','{}','{}')".format(qy_name,region_name,org_code,qy_id,fr_name,collect_time))
        conn.commit()
        cs.execute("select id from qy where qy_id='{}'".format(qy_id))
        get_id=cs.fetchall()[-1][0]
        url1='http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/getTotal?qyId={}&qyCode={}'.format(qy_id,org_code)
        return get_id,url1
    if total:
        ret=func(ret)
        ret=json.loads(ret)
        data=ret['data']
        xiangmu_total=data['proTotal']
        zhuce_total=data['ryTotal']
        url2="http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/regStaffList?qyId=2D2D2C2B2D2A2F2F2D2D282A2F2B2B2B292F&pg=0&pgsz={}".format(zhuce_total)
        url3="http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/compPerformanceListSys?qy_id=2D2D2C2B2D2A2F2F2D2D282A2F2B2B2B292F&pg=0&pgsz={}".format(xiangmu_total)
        return url2,url3
    if zhuce:
        t=func(ret)
        ret=json.loads(ret)
        data=ret['data']['pageList']['list']
        for i in data:
            REG_SDATE=int(i['REG_SDATE'])
            REG_SDATE=date(REG_SDATE)
            cs.execute("insert into zhuce values(0,'{}','{}','{}','{}','{}',{},'{}')".format(
                i['RY_NAME'],i['REG_TYPE_NAME'],i['REG_SEAL_CODE'],i['REG_PROF_NAME'],REG_SDATE,get_id,i['RY_CARDNO'])
            )
        conn.commit()
    if xiangmu:
        ret=func(ret)
        ret=json.loads(ret)
        data=ret['data']['list']
        for i in data:
            PROVINCE=i['PROVINCE'] if i['PROVINCE'] else ''
            CITY=i['CITY'] if i['CITY'] else ''
            COUNTY=i['COUNTY'] if i['COUNTY'] else ''
            location=PROVINCE+CITY+COUNTY
            cs.execute("insert into xiangmu values(0,'{}','{}','{}','{}','{}',{})".format(
                i['PRJNAME'],location,i['PRJTYPENUM'],i['BUILDCORPNAME'],i['PRJNUM'],get_id)
            )
        conn.commit()
        cs.close()
        conn.close()


ret=resp1(url)
get_id,url1=parse(ret,qy=1)

time.sleep(1)
ret=resp1(url1)
url2,url3=parse(ret,total=1)

time.sleep(1)
ret=resp1(url2)
parse(ret,zhuce=1)

time.sleep(1)
ret=resp1(url3)
parse(ret,xiangmu=1)
