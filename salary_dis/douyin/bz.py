import os
import re

import requests
import json
from lxml import etree

header = {
    "referer": "https://www.bilibili.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

def get_play_url(url):
    r = requests.get(url, headers=header)
    info = re.findall('window.__playinfo__=(.*?)</script>', r.text)[0]
    video_url = json.loads(info)["data"]["dash"]["video"][0]["baseUrl"]
    audio_url = json.loads(info)["data"]["dash"]["audio"][0]["baseUrl"]
    html = etree.HTML(r.text)
    filename = html.xpath('//h1/text()')[0]
    return video_url, audio_url, filename

def download_files(video_url, audio_url, filename, video_path, audio_path):
    print("开始下载视频和音频")
    video_content = requests.get(video_url, headers=header).content
    audio_content = requests.get(audio_url, headers=header).content

    with open(f'{video_path}/{filename}.mp4', 'wb') as f:
        f.write(video_content)
        print("视频部分下载完毕")
    with open(f'{audio_path}/{filename}.mp3', 'wb') as f:
        f.write(audio_content)
        print("音频部分下载完毕")

def combin_video_audio(filename, video_path, audio_path):
    cmd = fr"D:\ApplicationsSoftware\FFmpeg\ffmpeg-7.1-full_build\ffmpeg-7.1-full_build\bin\ffmpeg -i {video_path}/{filename}.mp4 -i {audio_path}/{filename}.mp3 -c:v copy -c:a aac -strict experimental -map 0:v -map 1:a {video_path}/output-{filename}.mp4 -loglevel quiet"
    os.system(cmd)
    print("音频视频合并完毕")
    print("--" * 10)
    os.remove(f'{video_path}/{filename}.mp4')
    os.remove(f'{audio_path}/{filename}.mp3')
    print('已删除多余的文件')

if __name__ == '__main__':
    my_documents_path = os.path.expanduser("~\Documents")
    video_path = os.path.join(my_documents_path, "video", "videos")
    audio_path = os.path.join(my_documents_path, "video", "audio")

    if not os.path.exists(video_path):
        os.makedirs(video_path)
    if not os.path.exists(audio_path):
        os.makedirs(audio_path)

    url = 'https://m.bilibili.com/video/BV1wNkqYWEZw?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=25b09eebc67955e9bc0e544ff3123a9f'
    video_url, audio_url, filename = get_play_url(url)
    download_files(video_url, audio_url, filename, video_path, audio_path)
    combin_video_audio(filename, video_path, audio_path)