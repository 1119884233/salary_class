import os

import data_get

from data_save import data_save


def main():
    url="9-0-0-ad482007aa7e8b110354fdaa506ce358&bcevod_channel=searchbox_feed&cr=0&cd=0&pd=1&pt=3&logid=2989173713&vid=3250368275852509710&klogid=2989173713&abtest=.mp4"
    content=data_get.get_content_no_headers(url)
#保持视频
    data_save.save_content("video_tlb.mp4",content)


if __name__ == '__main__':
    main()