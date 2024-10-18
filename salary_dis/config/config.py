
def pic_params(pic_page,pic_name):
    img_url="https://images.baidu.com/search/acjson?tn=resultjson_com&logid=11368488687042505277&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E9%B8%A1%E8%9B%8B&queryWord=%E9%B8%A1%E8%9B%8B&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1729220577662="
    img_headers={
    "accept":"text/plain, */*; q=0.01",
    "accept-encoding":"gzip, deflate, br, zstd",
    "accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "connection":"keep-alive",
    "cookie":'"BAIDUID_BFESS=396F8F3A35B261A8E2391D16F53CCC1F:FG=1; MAWEBCUID=web_bSWRRkNYqILhZSIPIIpPVFJMHKHFntagIUArQJgoNbyoGQXYAX; __bid_n=18b4fd6e9cc1152a8e283b; ZFY=XO7Q7pwLmYcJUEhnSM:Bmv:A:B9vezsJWj7BP1GYwxlEps:C; BIDUPSID=396F8F3A35B261A8E2391D16F53CCC1F; PSTM=1706684469; H_WISE_SIDS=60289; H_WISE_SIDS_BFESS=60289; H_PS_PSSID=60277_60599_60630_60665_60616_60694_60724; RT="z=1&dm=baidu.com&si=ae7e42b2-4c12-47a8-a964-907a584052c1&ss=m25fuirb&sl=1u&tt=1jqd&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=6o03w"; SEARCH_MARKET_URL=http%3A//wenku.baidu.com/ndlaunch/browse/chat%3Ffr%3Dlaunch_ad%26utm_source%3Dbdss-WD%26utm_medium%3Dcpc%26keyword%3D%25E7%2599%25BE%25E5%25BA%25A6%25E6%2596%2587%25E6%25A1%25A3%25E5%258A%25A9%25E6%2589%258B%26utm_account%3DSS-bdtg160%26e_creative%3D80905950322%26e_keywordid%3D660796825044%26bd_vid%3D2413308120939340485; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E9%B8%A1%E8%9B%8B%22%2C%22%E5%9B%BE%E7%89%87%22%2C%22%E5%9B%BE%E7%89%87%E7%BE%8E%E5%A5%B3%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=images.baidu.com; ab_sr=1.0.1_NzdlYWIzODNlYzlhMDExMTUzZmY2NTU4ZGRiNTdkYTE2NjViMmRlNmM1MjAwNTMzYWNmNGY5MWZlYTFlOGFiZDE4MzdmNTQxNTQ5ODdlZjA4NGM1MTZlYTBmZGM0NWNiZmQ1YjFjYmY3MjI4ZTQ2MWQ3ZGY1ZmIzZWY1YTVjMmRmNjM5YTU3NzE2ZWZhOWY1ZWM0MWI1ZjliMjJkNmE4YQ==; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm"',
    "host":"images.baidu.com",
    "referer":"https://images.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%B8%A1%E8%9B%8B&oq=%E9%B8%A1%E8%9B%8B&rsp=-1",
    "sec-ch-ua":'"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":'"Windows"',
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "x-requested-with":"XMLHttpRequest"
    }


def params(pic_page,pic_name):
        params={
        "tn":"resultjson_com",
        "logid":"11368488687042505277",
        "ipn":"rj",
        "ct":"201326592",
        "is":"",
        "fp":"result",
        "fr":"word: 鸡蛋",
        "queryWord":"鸡蛋",
        "cl":"2",
        "lm":"-1",
        "ie":"utf-8",
        "oe":"utf-8",
        "adpicid":"",
        "st":"-1",
        "z":"",
        "ic":"0",
        "hd":"",
        "latest":"",
        "copyright":"",
        "s":"",
        "se":"",
        "tab":"",
        "width":"",
        "height":"",
        "face":"0",
        "istype":"2",
        "qc":"",
        "nc":"1",
        "expermode":"",
        "nojc":"",
        "isAsync":"",
        "pn":"30",
        "rn":"30",
        "gsm":"1e",

    }
        return img_url

#定义存储图片的地址
img_file="../img_data/"