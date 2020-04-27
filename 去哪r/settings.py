# 输入搜索日期，地址不提供修改
departureDate='2020-04-29'

l1="""const jsdom = require("/usr/local/lib/node_modules/jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><script>window.__root_time = new Date().getTime();</script><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="pragma" content="no-cache"><meta http-equiv="cache-control" content="no-cache"><meta name="Robots" content="index,follow"><meta http-equiv="X-UA-Compatible" content="edge" /><meta name="septem" content="ber" /><meta name="description" content="去哪儿(Qunar.com)作为全球最大的中文旅游搜索引擎,通过对机票,酒店,旅游线路的整合与发布,提供专业、实时、可信的旅游产品价格比较与服务比较系统,帮助消费者轻松进行充分选择,是您预订机票、酒店、旅游线路的最佳选择!"><meta name="wuvwrlnrvq" content="vjvq" ></meta><meta name="keywords" content="机票酒店预订预定打折优惠特价比价,打折机票,特价机票,电子机票,机票查询,航班查询,国际机票,联程航班,酒店预订,宾馆预订,酒店打折,酒店价格,酒店博客,国际机票预定,国际酒店预定,Qunar.com"><title>【去哪儿网】机票查询,特价机票,打折飞机票-去哪儿网Qunar.com</title><meta name="dece" content="mber" />  
<link rel="stylesheet" href="//q.qunarzz.com/flight_qzz/prd/header@adf85c2e95754fb6c36d.css">
<link rel="stylesheet" href="//q.qunarzz.com/flight_qzz/prd/domestic_oneway_new@569b330b8ec4cb0bf9a2.css">
<link rel="stylesheet" href="//q.qunarzz.com/flight_qzz/prd/rightSidebar@02cd509c913ae1e67cdf.css">
<link rel="stylesheet" href="//q.qunarzz.com/flight_qzz/prd/footer@e48f4ef92d96ca5688f5.css">
<link rel="stylesheet" href="//q.qunarzz.com/quinn/prd/qsl@49c498fd2608cdfccc1d.css">
`,{url:"https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E9%95%BF%E6%B2%99&searchArrivalAirport=%E4%B8%8A%E6%B5%B7&searchDepartureTime=2020-04-30&searchArrivalTime=2020-04-25&nextNDays=0&startSearch=true&fromCode=CSX&toCode=SHA&from=flight_dom_search&lowestPrice=null"});
window = dom.window;
document = window.document;
location=window.location
XMLHttpRequest = window.XMLHttpRequest;"""

