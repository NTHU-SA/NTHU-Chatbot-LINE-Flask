from linebot import LineBotApi, WebhookHandler
from API import TokenAPI, UserAPI

mode = 'official' # 只要改這個模式就好

# 取得 token & webhook
# t = TokenAPI()
# token, webhook, _ = t.getAuth(mode)

# official:
token = '${LINE_OFFICIAL_TOKEN}'
webhook = '${LINE_WEBHOOK_STRING}'

# beta:
# token = 'BETA_TOKEN'
# webhook = 'WEBHOOK_STRING'

print('token:', token)
print('webhook:', webhook)


# Beta Chatbot
line_bot_api = LineBotApi(token)
handler = WebhookHandler(webhook)

# user instance
user = UserAPI()
