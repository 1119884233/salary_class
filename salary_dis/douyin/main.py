import requests
cookies = {
    'buvid3': 'A02E7647-6DFD-E7ED-47C4-7472A53A74A535400infoc',
    'b_nut': '1727598635',
    '_uuid': '16375F45-C5DB-F3CA-A989-10D6ACF105C76E35219infoc',
    'enable_web_push': 'DISABLE',
    'buvid4': '4701039C-803D-911B-0440-90D565BD80EB36583-024092908-fcASUcpyhjGK9py2pG6QZA%3D%3D',
    'buvid_fp': '7ebe15a912a3b9d49babbd065651ccd9',
    'rpdid': "|(k|JJumY|lY0J'u~k~lm)Yll",
    'DedeUserID': '3546637194496604',
    'DedeUserID__ckMd5': '75eeaf6bb69fc726',
    'header_theme_version': 'CLOSE',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ4MzM3MDUsImlhdCI6MTczNDU3NDQ0NSwicGx0IjotMX0.WkvUaDvxnRFbgU0Jm9rZEX804t33BndW51sRCHHz8YA',
    'bili_ticket_expires': '1734833645',
    'SESSDATA': '4199ad22%2C1750126508%2C972f9%2Ac1CjBqKK72IVfpYR1h8-FoArdiOVaOdDeXHdJDxvy_1tgjn7HEqPwF3n0iOo5JbbQkdDgSVnBaMlAweVZzMUt2cWRvSUhCdzFuMEo4WXNsZUJBRnpQeHBxM09ya05rZ3RFaS1abnhpUVZmbFV4U2hSRHNPcVNqZzlpWnpmSllMaTUzMGFoN1JMa0J3IIEC',
    'bili_jct': 'caba2065df986578fe57a9c1114145bc',
    'b_lsid': '106791AC8_193E1839751',
    'bsource': 'search_bing',
    'sid': '6wvauueu',
    'browser_resolution': '1243-727',
    'home_feed_column': '4',
    'CURRENT_FNVAL': '4048',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': "buvid3=A02E7647-6DFD-E7ED-47C4-7472A53A74A535400infoc; b_nut=1727598635; _uuid=16375F45-C5DB-F3CA-A989-10D6ACF105C76E35219infoc; enable_web_push=DISABLE; buvid4=4701039C-803D-911B-0440-90D565BD80EB36583-024092908-fcASUcpyhjGK9py2pG6QZA%3D%3D; buvid_fp=7ebe15a912a3b9d49babbd065651ccd9; rpdid=|(k|JJumY|lY0J'u~k~lm)Yll; DedeUserID=3546637194496604; DedeUserID__ckMd5=75eeaf6bb69fc726; header_theme_version=CLOSE; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ4MzM3MDUsImlhdCI6MTczNDU3NDQ0NSwicGx0IjotMX0.WkvUaDvxnRFbgU0Jm9rZEX804t33BndW51sRCHHz8YA; bili_ticket_expires=1734833645; SESSDATA=4199ad22%2C1750126508%2C972f9%2Ac1CjBqKK72IVfpYR1h8-FoArdiOVaOdDeXHdJDxvy_1tgjn7HEqPwF3n0iOo5JbbQkdDgSVnBaMlAweVZzMUt2cWRvSUhCdzFuMEo4WXNsZUJBRnpQeHBxM09ya05rZ3RFaS1abnhpUVZmbFV4U2hSRHNPcVNqZzlpWnpmSllMaTUzMGFoN1JMa0J3IIEC; bili_jct=caba2065df986578fe57a9c1114145bc; b_lsid=106791AC8_193E1839751; bsource=search_bing; sid=6wvauueu; browser_resolution=1243-727; home_feed_column=4; CURRENT_FNVAL=4048",
    'origin': 'https://www.bilibili.com',
    'priority': 'u=1, i',
    'referer': 'https://www.bilibili.com/video/BV1JS4y1W7GD/?spm_id_from=333.788.player.player_end_recommend_autoplay&vd_source=c299956f432211c93b9ab22b9000b695',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}
# time.sleep(10)
response = requests.get(
    'https://api.bilibili.com/x/v2/reply/wbi/main?oid=729645142&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=704f776a0d93398d0821c885ecb5bc45&wts=1734658097',
    cookies=cookies, headers=headers, )
response.encoding = 'utf-8'
items = response.json()['data']['replies']

for item in items:
    print(item['content']['message'])
