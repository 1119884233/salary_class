from sympy.physics.vector.printing import params
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
        return img_url,img_headers

# 定义存储图片的地址
img_file = "../img_data/"

# 定义想要抓取的工作类型
job_list = ["java","python","前端","教师","产品经理","深度学习","机器学习","销售","测试","算法","司机"]

# 自定义工作获取链接
def job_url(page_number,job_name):
    job_url="https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1729162015&keyword="+str(job_name)+"&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum="+str(page_number+1)+"&requestId=&keywordType=&pageSize=20&source=1&accountId=130412842&pageCode=sou%7Csou%7Csoulb"
    return job_url

job_headers = {
    "accept":"application/json, text/plain, */*",
    "accept-encoding":"gzip, deflate, br, zstd",
    "accept-language":"zh-CN,zh;q=0.9",
    "account-id":"239487025",
    "connection":"keep-alive",
    "cookie":"guid=b99c6603e8d8d2890b8997f1ade100f8; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=needv%3D0; 51job=cuid%3D239487025%26%7C%26cusername%3DNrUKLmJr6FueYjjofNI%252BOiHEUtRaDoklq8cUsrPAcyA%253D%26%7C%26cpassword%3D%26%7C%26cname%3D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0ltJHgAzWp9A%26%7C%26cconfirmkey%3D%25241%2524bZI3AiSy%2524XOpy1jczvR.fUB2rnEmcT1%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D%26%7C%26cnamekey%3D%25241%2524%252FuCqIQ0m%25246Q8IDcfaSeBa6ctFW6zRA%252F%26%7C%26to%3D1a4f54ffe0d17bdd2e3a389fb97fb805671f489e%26%7C%26; sensor=createDate%3D2024-01-29%26%7C%26identityType%3D2; adv=ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fpartner%253Dsem_pcbingbd_22675%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9MUF8yMDI0X0JDMS5odG1sP2Zyb209YmluZ2FkJnBhcnRuZXI9c2VtX3BjYmluZ2JkXzIyNjc1%2526k%253D70beee65b62821f3b4846c4b5feb8819%2526msclkid%253D10db6542f520128a80620269b8f238ed%26%7C%26; tfstk=fGGrws2yaQdz1uRCOzPFgp0CzNN8t7x6LXZQ-203PuqlNUHViyi7Ve3H2DlUm2c7quT8TJmnqDypykZ3YDgnFEO614389WxefCO_pkT5S0WhE6Y3myz9X45j34389ZE3KjpxyMzPuLi3tDV0nyUUtM4utEP0PzPhZJflniqYmkV3Ey0DiyaOqa4hEEu0DyV3xvN_t5I_S8Yt1XB4_N2bUl02B6fedzj_b4mAt6qzz88qro5htjkY4bAzqdQbv7Z-Tzop6_FuLA3Q80RPZDutMmzmjB5_qq3sC8hkd1waguyIZD-FLzks4DEorgXu77rzIb2ArEu4Kxl4NbxdBqg4qRPjhKK7d7orBlekHnnEuuina-jyckMslb2qjn1qvJktRyoya_mG46SLoUSI9YShL84YulT2uwYfcmSc11QGp9eRkrr6yJXdp84YulT2u9BLenU4fUeh.; partner=cn_bing_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fcn.bing.com%5C%2F%22%2C%22referHost%22%3A%22cn.bing.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; privacy=1732588945; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1731631668,1731917220,1732535325,1732588946; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1732588946; HMACCOUNT=29218FA959C12302; acw_tc=ac11000117325889495982482e00983e4175e823317aaea81b3a7ac9a1dce7; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22239487025%22%2C%22first_id%22%3A%2218f2d24799114ab-0336da24f1523e4-4c657b58-1638720-18f2d247992fdf%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmMmQyNDc5OTExNGFiLTAzMzZkYTI0ZjE1MjNlNC00YzY1N2I1OC0xNjM4NzIwLTE4ZjJkMjQ3OTkyZmRmIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMjM5NDg3MDI1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22239487025%22%7D%2C%22%24device_id%22%3A%2218f2d24799114ab-0336da24f1523e4-4c657b58-1638720-18f2d247992fdf%22%7D; slife=lastlogindate%3D20241126%26%7C%26securetime%3DAz9daVA1WT9SNQUzDD9cPgYwCj0%253D; acw_sc__v2=67453597d7f527b64f617903a0d9c7665decef27; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%CB%B9%A4%D6%C7%C4%DC%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%BF%AA%B7%A2%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%BE%FC%B6%D3%CE%C4%D6%B0%D0%C5%CF%A2%BC%BC%CA%F5%D4%B1%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA03%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%CB%B9%A4%D6%C7%C4%DC%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%FD%D1%A7%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; JSESSIONID=3967B983B16476E0FBE224DDF4662E6C; ssxmod_itna=iqmhq+x0xfxRx7qqBPxB4DKdO+DyDQqxw++w5KhvbH5DsYWDSxGKidDqxBnmZG4I3E7GhxqHex=xmqQUWQ7GdIth3cOieTDCPGnDBIApCDemtD5xGoDPxDeDAAqGaDb4DrnoqGp9uXvX6uDAQDQ4GyDitDKT09Di3DA4Dj8kDQGDw9bqG0DDtDAu0tqeDADA3B0DDl0AcWW7=QDYp9jLdePW2Nx2teiA=DjqGgDBdKYtutd/7QButzZaFHtuiqxBQD7LrS/brdGuNlYT93mSGo4+DF0fqQ7bxoYYI2D2qa8RmFR41bq3dxD=; ssxmod_itna2=iqmhq+x0xfxRx7qqBPxB4DKdO+DyDQqxw++w5Khvb5ik67Dlc4QIQ08D+hoD",
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
    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0",
    "user-token":"1a4f54ffe0d17bdd2e3a389fb97fb805671f489e",
    "uuid":"b99c6603e8d8d2890b8997f1ade100f8"
}

job_detail_headers={
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"accept-encoding":"gzip, deflate, br, zstd",
"accept-language":"zh-CN,zh;q=0.9",
"cache-control":"max-age=0",
"connection":"keep-alive",
"cookie":"guid=9f3339db587974f2a5b5cb76dabe7019; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=needv%3D0; 51job=cuid%3D130412842%26%7C%26cusername%3DEDL%252By52qLDKqDc%252BybOKm3aocYZ1uMgkLbiuW9AlQpj8%253D%26%7C%26cpassword%3D%26%7C%26cname%3DMKB53%252BalYHCaX%252BKUmzVDGQ%253D%253D%26%7C%26cemail%3Deei8Jb9o6%252BBmI5FZj1TkQfy9ie4oyrCFp4xfugZ9x5k%253D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0GYdOXnWZU%252Fs%26%7C%26cconfirmkey%3D27r9ie%252FZ2Fewc%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D1%26%7C%26cnamekey%3D27vUP4HX5195Y%26%7C%26to%3De3d23aa4f422f7a20ac85d893253e726670cb7db%26%7C%26; sensor=createDate%3D2017-08-29%26%7C%26identityType%3D1; tfstk=gKymQ1sPaSlXfxAS5gkfstqCKtC8cnMsJPptWA3Na4uWkSEZ0Y5gzPhaHxEYrAq_oqrtH1ao7yUiX-eT0luih8FvBqQjIlzKIwQdp9EbcXMNJwQW1KnKLDLw0F3qUTk11GSnX9Ebc3-D7MFPpFjf4kVq7PlqU3oZzm-47ISozcmB_EzZQgjoXc-2uml244oIAAua7ASu4AN1gqwaU87f_ULU6b5L3mcm8ou0DoezKe3305vMIbnmi_qqrdJaE7h3_Y0VO33sHqZjmP6Bhxlg_-Hz3aWZLWauIXkh6iMUhlPQ_uTcjqr8lJD4KZvx2f00a-lkbdrmFSlTsrbDGqPYrXirahXI2y3zc-PlfUr4JqDq4bBFxulaw-GQHaJmLWZxH5zFyI34tcSruQREO79s4Gey1CGqV00pmwMxyZAJr3SlqBSsg0ijJgjk1CGqV00dqgAFCjoSc2C..; partner=www_baidu_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3DTmaXz-i_eAjmz5Lz5IdKgOqFGm_Ht5j1FZy6X3qRD6m%26wd%3D%26eqid%3Ddee000e9001392ed000000036715be66%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; privacy=1729478310; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1728868251,1729161996,1729478314; HMACCOUNT=54908DEDB3194E6A; acw_tc=ac11000117294783122738378e0086c84b88cc2f70f9b995c4d99b64988154; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22130412842%22%2C%22first_id%22%3A%221928893f33f1d84-02a11d6d7e597a2-26001051-1327104-1928893f34017fb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyODg5M2YzM2YxZDg0LTAyYTExZDZkN2U1OTdhMi0yNjAwMTA1MS0xMzI3MTA0LTE5Mjg4OTNmMzQwMTdmYiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjEzMDQxMjg0MiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22130412842%22%7D%2C%22%24device_id%22%3A%221928893f33f1d84-02a11d6d7e597a2-26001051-1327104-1928893f34017fb%22%7D; slife=lastlogindate%3D20241021%26%7C%26securetime%3DADxUYFQwWTQAZgE4XW4JYVtpBjg%253D; acw_sc__v2=6715beb053bb4b2d0266ba3b8cd74d7651dee71b; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CB%BE%BB%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CF%FA%CA%DB%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B2%E2%CA%D4%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%CB%B9%A4%D6%C7%C4%DC%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B0%B2%B1%A3%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1729479229; ssxmod_itna=YqRx97D=9ODtDXKDHD0Q5iiQGk3ot+hx5GOQnG3TcDBTqAKYDZDiqAPGhDC4St2rPoaKDL4Q76QF8qjT6CABpTq6BWfbLj4TxB3DEx06bOKYeiiMDCeDIDWeDiDG4Gm4qGtDpxG=DjDytZ9TtDm4GWDeDg/4Gg3erD03NBWdrD4qDBfgdDKw2gfDDlfGn3FBQqieD+/32lBlUbWaq=GqDM7eGXGoy3GqT1g6+VWaF8=jPcDB=pxBjZInttv7UDguiobApxbD4hYx+mn7P5YYh3tEM+YcmqtOq=DgAeGoxFlzqXxD30uiqxD=; ssxmod_itna2=YqRx97D=9ODtDXKDHD0Q5iiQGk3ot+hx5GOQnG3cD8w1ikDGNUe4GaneXhvx8o2=Dc0LRNheg0gF4=RlhS9Uepzb1AIkpfSLWP6qn8BEK+mnSjets8QDthQ=831uv0jWpoCokSkwwuHpDvtlAaatmuh2rWFV6W7VcAFtYuFgmA=RmYrzouHsp0Dw1b10mwHalO1OaK5NObF/QiPot74f8vE4Id1u+wHwgu8tY7pscavtPekx6+pcg93jD076rGfz1wq30nDd119O21i+UebDjKD+ahDD",
"host":"jobs.51job.com",
"referer":"https://jobs.51job.com/guangzhou/154175168.html?s=sou_sou_soulb&t=0_0&req=c06c564753a37220f282d2a74fce8017",
"sec-ch-ua":'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform":'"Windows"',
"sec-fetch-dest":"document",
"sec-fetch-mode":"navigate",
"sec-fetch-site":"same-origin",
"sec-fetch-user":"?1",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
# excel_first_row
first_row = ["工作名称","公司名称","工作地点","学历要求","岗位要求","薪资待遇"]

# 数据库数据
def mysql_info():
    host="localhost"
    user="root"
    passwd="123456"
    db = "user_info"
    # db="51job2"
    return host,user,passwd,db

#  ************************ 定义neo4j参数 ****************************
neo4j_user = "neo4j"
neo4j_password = "WXZyzx20041018"


job_name=["android开发","java开发","交通运输","前端开发","医生","后端开发","房地产","护士","教师","机器学习","深度学习","算法工程师","自然语言处理"]

