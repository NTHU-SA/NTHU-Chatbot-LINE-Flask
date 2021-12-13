from linebot.models import *

def ans_and_confirm_btn(ans):
    template_list = []
    
    text_template = TextSendMessage(text=ans)

    confirm_template = TemplateSendMessage(
        alt_text='是否要繼續向本汪提問',
        template=ConfirmTemplate(
            title='是否要繼續向本汪提問關於校務的問題呢？',
            text='是否要繼續向本汪提問關於校務的問題呢？',
            actions=[                              
                PostbackTemplateAction(
                    label='不用了',
                    data='source=none&flag=stop&info=qa'
                ),
                PostbackTemplateAction(
                    label='繼續提問',
                    data='source=richmenu&flag=affair&info=qa'
                ),
            ]
        )
    )

    template_list.append(text_template)
    template_list.append(confirm_template)

    return template_list
