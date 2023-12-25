from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from datetime import datetime,timezone,timedelta
import re


app = Flask(__name__)
line_bot_api = LineBotApi("LINE_CHANNEL_ACCESS_TOKEN")
line_handler = WebhookHandler("LINE_CHANNEL_SECRET")

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def Pre01():
        flex_message = FlexSendMessage(
    alt_text='地圖',
    contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "小南門",
            "weight": "bold",
            "size": "sm",
            
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "餐廳",
                    
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "show map",
              "text": "小南門"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "塔美爾尼泊爾咖哩",
            "weight": "bold",
            "size": "sm",
            
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "餐廳",
                    
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "show map",
              "text": "塔美爾尼泊爾咖哩"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "大戶屋",
            "weight": "bold",
            "size": "sm"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "餐廳",
                    
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "show map",
              "text": "大戶屋"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
}
)
            
        return flex_message


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    myT=event.message.text        
    if myT == "map":
        P01 = Pre01()       
        line_bot_api.reply_message(event.reply_token,P01)
    elif myT == "小南門":
        P01 = Pre01()       
        line_bot_api.reply_message(event.reply_token, LocationSendMessage(title='Location message test', address='小南門', latitude = 25.048031, longitude = 121.517356))
        
    elif myT == "塔美爾尼泊爾咖哩":
        P01 = Pre01()       
        line_bot_api.reply_message(event.reply_token, LocationSendMessage(title='Location message test', address='塔美爾尼泊爾咖哩', latitude = 25.047924, longitude = 121.517131))

    elif myT == "大戶屋":
        P01 = Pre01()       
        line_bot_api.reply_message(event.reply_token, LocationSendMessage(title='Location message test', address='大戶屋', latitude = 25.047924, longitude = 121.51708))
   
    else:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=myT)])


if __name__ == "__main__":
    app.run()
