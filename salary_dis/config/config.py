# from sympy.physics.vector.printing import params
def pic_params(pic_page,pic_name):
        img_url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7475088676751279302&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word="+pic_name+"&queryWord="+pic_name+"&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn="+str(pic_page)+"&rn=30&gsm=1e&1729220216920="
        img_headers={
        "accept":"text/plain, */*; q=0.01",
        "accept-encoding":"gzip, deflate, br, zstd",
        "accept-language":"zh-CN,zh;q=0.9",
        "connection":"keep-alive",
        "cookie":"BDqhfp=%E9%B8%A1%E8%9B%8B%26%26NaN-1undefined%26%260%26%261; BIDUPSID=B3D872A421BEE39C1682881E69AFE8C6; PSTM=1728521611; H_WISE_SIDS_BFESS=60449_60843; newlogin=1; BDUSS=jVMaEljTjFIS2NvT0RkUEdScGpVMlFvWXdDOWxXaGF6cWl4QUVJa1RSNElCalJuRUFBQUFBJCQAAAAAAAAAAAEAAACTCa0hztK6zcO3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAh5DGcIeQxnM; BDUSS_BFESS=jVMaEljTjFIS2NvT0RkUEdScGpVMlFvWXdDOWxXaGF6cWl4QUVJa1RSNElCalJuRUFBQUFBJCQAAAAAAAAAAAEAAACTCa0hztK6zcO3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAh5DGcIeQxnM; H_PS_PSSID=60449_60843_60853_60886_60875; H_WISE_SIDS=60449_60843_60853_60886_60875; BAIDUID=B3D872A421BEE39CB9C94E2D5F05C5D6:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=0g8k0k2g018h0k0500a1a004ao840u1jh21pc1u; BAIDUID_BFESS=B3D872A421BEE39CB9C94E2D5F05C5D6:SL=0:NR=10:FG=1; ZFY=r:BJGX6OuT4WGq1Kw2grh6ccOKmVQiF5FJwAHUvqnG:Bg:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; delPer=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_MTNiZmIyNDgwOTdjOWM3NmQ5ZTY5ZDA2Y2EzMjBjMzM2YTQ4ZWIzOGZjN2EzNTdkMzU1MjEzZTRkNzQyMmUxYjNiNTk0ZDM4NDc1OWE0ODhiMzc4OWMxNWVjMmQzMzU1NTcwOWE3MTRmNTA0NTU2MjA3Yzk3MGFkMWE1YzU2NTkzMmU2ZGVkNzM0MzFkZmY1NmY1ZmZkYjdmZDQ1ZDVkMA==",
        "host":"image.baidu.com",
        "referer":"https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=utf8&word=%E9%B8%A1%E8%9B%8B&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCwzLDEsMiwxMyw3LDYsNSwxMiw5",
        "sec-ch-ua":'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":'"Windows"',
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "x-requested-with":"XMLHttpRequest"
        }
        params={
        "tn":"resultjson_com",
        "logid":"7475088676751279302",
        "ipn":"rj",
        "ct":"201326592",
        "fp":"result",
        "fr":"ala",
        "word":str(pic_name),
        "queryWord":str(pic_name),
        "cl":"2",
        "lm":"-1",
        "ie":"utf-8",
        "oe":"utf-8",
        "pn":str(pic_page),
        "rn":"30",
        "gsm": "1e"
        }
        return img_url,img_headers,params

# 定义存储图片的地址
img_file = "../img_data/"

# 定义想要抓取的工作类型
job_list = ["java开发","前端开发","教师","产品经理","深度学习工程师","机器学习工程师","销售","安保","测试工程师","人工智能算法工程师","司机"]

# 自定义工作获取链接
def job_url(page_number,job_name):
    job_url="https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1729162015&keyword="+str(job_name)+"&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum="+str(page_number+1)+"&requestId=&keywordType=&pageSize=20&source=1&accountId=130412842&pageCode=sou%7Csou%7Csoulb"
    return job_url

job_headers = {
    "accept":"application/json, text/plain, */*",
    "accept-encoding":"gzip, deflate, br, zstd",
    "accept-language":"zh-CN,zh;q=0.9",
    "account-id":"130412842",
    "connection":"keep-alive",
    "cookie":"guid=9f3339db587974f2a5b5cb76dabe7019; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=needv%3D0; 51job=cuid%3D130412842%26%7C%26cusername%3DEDL%252By52qLDKqDc%252BybOKm3aocYZ1uMgkLbiuW9AlQpj8%253D%26%7C%26cpassword%3D%26%7C%26cname%3DMKB53%252BalYHCaX%252BKUmzVDGQ%253D%253D%26%7C%26cemail%3Deei8Jb9o6%252BBmI5FZj1TkQfy9ie4oyrCFp4xfugZ9x5k%253D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0GYdOXnWZU%252Fs%26%7C%26cconfirmkey%3D27r9ie%252FZ2Fewc%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D1%26%7C%26cnamekey%3D27vUP4HX5195Y%26%7C%26to%3De3d23aa4f422f7a20ac85d893253e726670cb7db%26%7C%26; sensor=createDate%3D2017-08-29%26%7C%26identityType%3D1; tfstk=gKymQ1sPaSlXfxAS5gkfstqCKtC8cnMsJPptWA3Na4uWkSEZ0Y5gzPhaHxEYrAq_oqrtH1ao7yUiX-eT0luih8FvBqQjIlzKIwQdp9EbcXMNJwQW1KnKLDLw0F3qUTk11GSnX9Ebc3-D7MFPpFjf4kVq7PlqU3oZzm-47ISozcmB_EzZQgjoXc-2uml244oIAAua7ASu4AN1gqwaU87f_ULU6b5L3mcm8ou0DoezKe3305vMIbnmi_qqrdJaE7h3_Y0VO33sHqZjmP6Bhxlg_-Hz3aWZLWauIXkh6iMUhlPQ_uTcjqr8lJD4KZvx2f00a-lkbdrmFSlTsrbDGqPYrXirahXI2y3zc-PlfUr4JqDq4bBFxulaw-GQHaJmLWZxH5zFyI34tcSruQREO79s4Gey1CGqV00pmwMxyZAJr3SlqBSsg0ijJgjk1CGqV00dqgAFCjoSc2C..; partner=www_baidu_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3DtQJb0pCvqKzeYqBqDbVFxiDT4_tX0To9lWH1Fqi0J3m%26wd%3D%26eqid%3Dae3a2f0b00037990000000036710eb03%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; privacy=1729161994; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1728868251,1729161996; HMACCOUNT=54908DEDB3194E6A; slife=lastlogindate%3D20241017%26%7C%26securetime%3DVmpVYVI2VjtfPAc%252FWGFeNVRnUGc%253D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22130412842%22%2C%22first_id%22%3A%221928893f33f1d84-02a11d6d7e597a2-26001051-1327104-1928893f34017fb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyODg5M2YzM2YxZDg0LTAyYTExZDZkN2U1OTdhMi0yNjAwMTA1MS0xMzI3MTA0LTE5Mjg4OTNmMzQwMTdmYiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjEzMDQxMjg0MiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22130412842%22%7D%2C%22%24device_id%22%3A%221928893f33f1d84-02a11d6d7e597a2-26001051-1327104-1928893f34017fb%22%7D; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CB%BE%BB%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B2%E2%CA%D4%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%CB%B9%A4%D6%C7%C4%DC%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B0%B2%B1%A3%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CF%FA%CA%DB%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; JSESSIONID=2EF6CDB8CEDBB7194CE39FD14EB1580F; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1729166143; acw_tc=ac11000117291671259425530e0077d4351c6304f7e8a64dedf2dc06bc3aa5; ssxmod_itna=Qq+xcQit5Cq4zxmxB4DIOlr72P0KK+YiD8YstoDBMBxiNDnD8x7YDvzmox0Ebf3+h3KQAbBD=YlA8v5bjW46+fE/YlD0aDbqGkqRe25GGjxBYDQxAYDGDDPDo2PD1D3qDkD7O1lS9kqi3DbONDmTdDIq0xxDdSFLQ4xYQDGqK6D7jq1L4D0L+NLGeNeuwxxGY6YmUdpkDToGGcD0UqxBdqf6+cInFCLiNT1P9DaEQDzu7Dtut5wMRoCwXM4W+v+Bes+7v53+G49oxbf7DvmiA39rxNYHq4YhhhY2DbUS3LzA4DG4oLeD; ssxmod_itna2=Qq+xcQit5Cq4zxmxB4DIOlr72P0KK+YiD8YsYx8dpCGeGXPGa7mkhLZ+jwzx0rIh8q7m407azx7=D+arD===; acw_sc__v2=6710ff183470654242a1a9c497dc97c4664fd5d6",
    "from-domain":"51job_web",
    "host":"we.51job.com",
    "partner":"www_baidu_com",
    "property":"%7B%22partner%22%3A%22www_baidu_com%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D000000%26keyword%3D%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD%26searchType%3D2%26keywordType%3D%22%2C%22identityType%22%3A%22%E8%81%8C%E5%9C%BA%E4%BA%BA%22%2C%22userType%22%3A%22%E8%80%81%E7%94%A8%E6%88%B7%22%2C%22isLogin%22%3A%22%E6%98%AF%22%2C%22accountid%22%3A%22130412842%22%2C%22keywordType%22%3A%22%22%7D",
    "referer":"https://we.51job.com/pc/search?jobArea=000000&keyword=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&searchType=2&keywordType=",
    "sec-ch-ua":'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":'"Windows"',
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "sign":"42a419f005eee5af58748f1f2f3213da2abbd0f8888154aecda4098daf40ad21",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "user-token":"e3d23aa4f422f7a20ac85d893253e726670cb7db",
    "uuid":"9f3339db587974f2a5b5cb76dabe7019"
}


def params():
    return None