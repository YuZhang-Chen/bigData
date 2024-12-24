from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
from get_data import get_data
app = Flask(__name__)

# Your Channel Access Token
LINE_CHANNEL_ACCESS_TOKEN = 'VP2lsLvpt4AaRKcHyDEcTIlLSgwyhcg/cnpGZRa1Xopc9zNVF/LpA3Y8abIlFVtNk8d0QI96ys7aBNN8i18/dbs03f6JtIDMl18IbYhhHvK5rNkw6LFRDBwi4ZSZhSvYnHwJP6P8GEIutaLPHRDPvgdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '796b39da34eee663cf8df2a09ffdb37e'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_input = event.message.text
    image_path, keyword, words_repo = get_data(user_input)
    
    line_bot_api.reply_message(
        event.reply_token, [
            ImageSendMessage(original_content_url=image_path, preview_image_url=image_path)
        ]
    )

if __name__ == "__main__":
    app.run(port=8000)