import pandas as pd
import requests
import os
import sys
import unidecode

try:
    from dotenv import load_dotenv, find_dotenv

    load_dotenv(find_dotenv())
except Exception as err:
    print(err)

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from python_scripts.open_ai import openAI

slack_app_token = os.environ.get("SLACK_APP_TOKEN", "")
slack_bot_token = os.environ.get("SLACK_BOT_TOKEN", "")
slack_dall_e_channel_id = os.environ.get("DALL_E_CHANNEL_ID", "")
slack_chat_gpt_channel_id = os.environ.get("CHAT_GPT_CHANNEL_ID", "")
app = App(token=slack_bot_token)

class bot():
    def __init__(self) -> None:
        try:
            handler = SocketModeHandler(app,slack_app_token)
            handler.start()
            print("running...")
        except Exception as err:
            print(err)
    @app.event("message")
    def listen(body,say):
        event = body["event"]
        channel_id = event["channel"]
        msg = event["text"]
        msg = msg.lower()
        thread_id = event.get("thread_ts", None) or event["ts"]
        if "dalle" in msg and channel_id == slack_dall_e_channel_id:
            text = msg.split(":")[1]
            print("mensaje detectado")
            print("texto a enviar: {}".format(text))
            dalle = openAI()
            url = dalle.text_to_image_url(text)
            dalle.url_to_image(url=url)
            dalle.send_message(thread_id=thread_id)
        elif "dalle" not in msg and channel_id == slack_chat_gpt_channel_id:
            dali = openAI()
            dali.chatGPT(text=msg,thread_id=thread_id)
        else:
            pass

