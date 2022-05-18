from linebot.models import *

def broadcast_info(toggle):
    if toggle:
        return TemplateSendMessage(
            alt_text='是否開啟主動推播？',
            template=ButtonsTemplate(
                title='是否開啟主動推播？',
                thumbnail_image_url='https://raw.githubusercontent.com/NTHU-SA/NTHU-Campus-Agent-LINE-Flask/master/images/Richmenu-images/on-cropped.png',
                image_aspect_ratio='square',
                image_size='contain',
                text='目前主動推播已開啟',
                actions=[
                    MessageAction(label = "確認關閉主動推播", text = "[選單]關閉主動推播")
                ]
            )
        )
    else:
        return TemplateSendMessage(
            alt_text='是否開啟主動推播？',
            template=ButtonsTemplate(
                title='是否開啟主動推播？',
                thumbnail_image_url='https://raw.githubusercontent.com/NTHU-SA/NTHU-Campus-Agent-LINE-Flask/master/images/Richmenu-images/off-cropped.png',
                image_aspect_ratio='square',
                image_size='contain',
                text='目前主動推播已關閉',
                actions=[
                    MessageAction(label = "確認開啟主動推播", text = "[選單]開啟主動推播")
                ]
            )
        )
