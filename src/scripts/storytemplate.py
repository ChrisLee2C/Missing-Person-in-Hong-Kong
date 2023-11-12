import cv2 as cv
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from config import *

class Story:
    def __init__(self,bgra,content_width,font_body_size,font_heading_size,font_family_path,story_heading,story_heading_height,story_dimension,
                 textbox_margin,text_body_position):
        self.bgra=bgra
        self.content_width=content_width
        self.font_body_size=font_body_size
        self.font_heading_size=font_heading_size
        self.font_family_path=font_family_path
        self.story_heading=story_heading
        self.story_heading_height=story_heading_height
        self.story_height=story_dimension[0]
        self.story_width=story_dimension[1]
        self.textbox_margin=textbox_margin
        self.text_body_x=text_body_position[0]
        self.text_body_y=text_body_position[1]

        self.font_body=ImageFont.truetype(self.font_family_path,self.font_body_size)
        self.font_heading=ImageFont.truetype(self.font_family_path,self.font_heading_size)
        self.story_heading_width=self.font_heading.getlength(self.story_heading)

    def image_resize(self,image):
        width=image.shape[1]
        height=image.shape[0]
        aspect_ratio=width/height
        if aspect_ratio>1:
            if width!=self.content_width:
                width=self.content_width
                height=int(width/aspect_ratio)
        else:
            if height!=self.content_width:
                height=self.content_width
                width=int(height*aspect_ratio)
        image=cv.resize(image,(width,height))
        return image

    def wrap_text(self,tags,personal_info):
        content=full_content=""
        lines=[]
        tag_length=self.font_body.getlength(tags)
        for character in personal_info:
            if character is None:
                character="None"
            if self.font_body.getlength(content+character)>self.content_width-tag_length:
                lines.append(content)
                content=character
                tag_length=0
            else:
                content+=character
        for sub_string in lines:
            full_content+=sub_string+"\n"
        full_content+=content
        final_text=tags+full_content+"\n"
        return final_text

    def set_body(self,tags,personal_info):
        body_text=""
        for i in range(len(personal_info)):
            body_text+=self.wrap_text(tags=tags[i],personal_info=personal_info[i])
        return body_text

    def create_story(self,image,tags,personal_info,story_path):
        if len(image.shape)!=2:
            story=np.ones((self.story_height,self.story_width,image.shape[2]),dtype=np.uint8)*255
        else:
            story=np.ones((self.story_height,self.story_width,2),dtype=np.uint8)*255
        img_pil=Image.fromarray(story)
        draw=ImageDraw.Draw(img_pil)
        heading_x,heading_y=(self.story_width-self.story_heading_width)/2,self.story_heading_height
        text_body=self.set_body(tags=tags,personal_info=personal_info)
        draw.text((heading_x,heading_y),self.story_heading,font=self.font_heading,fill=self.bgra)
        draw.text((self.text_body_x,self.text_body_y),text_body,font=self.font_body,fill=self.bgra,align="left")
        story=np.array(img_pil)
        resized_image=self.image_resize(image)
        height,width=resized_image.shape[0],resized_image.shape[1]
        offset_width_from,offset_width_to=int((self.story_width-width)/2),int((self.story_width+width)/2)
        offset_height_from,offset_height_to=int(self.textbox_margin+(self.content_width-height)/2),int(self.textbox_margin+(self.content_width+height)/2)
        story[offset_height_from:offset_height_to,offset_width_from:offset_width_to]=resized_image
        cv.imwrite(story_path,story)