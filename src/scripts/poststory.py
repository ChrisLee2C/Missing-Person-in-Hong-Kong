from getdatafile import *
from facebookapi import *
from config import *
from getdatafile import *
from driver import get_driver
from storytemplate import Story
from datetime import date
from driverautoupdate import *
import cv2 as cv
import numpy as np
import sys

if __name__=="__main__":
    local_version=get_local_version()
    print(f"Local version is {local_version}")
    current_stable_version=get_current_stable_version()
    if local_version != current_stable_version:
        zip_url=get_zip_download_url(current_stable_version=current_stable_version)
        extract_zip(zip_url=zip_url)
    else:
        print("pass")
    story_path_list=[]
    if len(sys.argv)>1:
        start=sys.argv[1]
    else:
        start=0
    root=data_request_get()
    story=Story(bgra=BGRA,
                content_width=CONTENT_WIDTH,
                font_body_size=FONT_BODY_SIZE,
                font_heading_size=FONT_HEADING_SIZE,
                font_family_path=FONT_FAMILY_PATH,
                story_heading=STORY_HEADING,
                story_heading_height=STORY_HEADING_HEIGHT,
                story_dimension=STORY_DIMENSION,
                textbox_margin=TEXTBOX_MARGIN,
                text_body_position=TEXT_BODY_POSITION)
    story_path_temp=STORY_PATH+f"story_{date.today()}_"
    #最近48名失蹤者，Facebook Story最大數量50，2個Story作爲時間Buffer
    for num in range(start,FB_STORY_AMOUNT_LIMIT):
        story_path=story_path_temp+str(num)+".png"
        resp=requests.get(HEAD_URL+root[num][9].text).content
        nparr=np.frombuffer(resp,np.uint8)
        image=cv.imdecode(nparr,cv.IMREAD_UNCHANGED)
        #personal_info=({國籍/性別 名字},{特徵},{衣服},{失蹤日期},{失蹤詳情},{聯絡方法})
        personal_info=(str(root[num][1].text),str(root[num][2].text),str(root[num][5].text),str(root[num][3].text),
                       str(root[num][6].text),str(root[num][7].text))
        story.create_story(image=image,tags=TAGS,personal_info=personal_info,story_path=story_path)
        print(f"Created story {num}")
        story_path_list.append(story_path)
        story_path=story_path_temp
    driver=get_driver()
    driver=login(driver=driver,link=FB_URL,username=FB_USERNAME,password=FB_PASSWORD)
    post_story(driver=driver,story_path_list=story_path_list)
    print("Post story ends")