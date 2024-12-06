import requests

url = "https://bimp.hdslb.com/videoshotpvhdboss/26428705262_h920eb-0001.jpg@3200w_1800h_50q.avif"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'referer': 'https://www.bilibili.com/video/BV1EUyoYkE8v/?spm_id_from=333.1007.tianma.2-1-4.click'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open('我的视频.mp4', 'wb') as f:
        f.write(response.content)
    print("视频下载成功！")
else:
    print("视频下载失败，错误代码:", response.status_code)
