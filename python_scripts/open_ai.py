import pandas as pd
import requests
import os
import sys
from PIL import Image
from urllib.request import urlopen
import unidecode

try:
    from dotenv import load_dotenv, find_dotenv

    load_dotenv(find_dotenv())
except Exception as err:
    print(err)


from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack import WebClient
import openai

openai.api_key = os.environ.get("OPEN_AI_API_KEY", "")


class openAI():
    def __init__(self) -> None:
        self.slack_bot_token = os.environ.get("SLACK_BOT_TOKEN", "")
        self.slack_app_token = os.environ.get("SLACK_APP_TOKEN", "")
        self.slack_dall_e_channel_id = os.environ.get("DALL_E_CHANNEL_ID", "")
        self.slack_web_client = WebClient(token=self.slack_bot_token)
        self.slack_chat_gpt_channel_id = os.environ.get("CHAT_GPT_CHANNEL_ID", "")

    def text_to_image_url(self, text, size="512x512"):
        response_url = openai.Image.create(prompt=text, n=1, size=size)
        return response_url["data"][0]["url"]

    def url_to_image(self,url):
        img = Image.open(urlopen(url=url))
        return img.save("dall-e.png")

    def send_message(self,thread_id=None):
        self.slack_web_client.chat_postMessage(
            channel=self.slack_dall_e_channel_id,
            username="Dall-E",
            text="Dall-E está preparando tu imagen",
            thread_ts=thread_id
        )
        self.slack_web_client.files_upload(
            channels=self.slack_dall_e_channel_id,
            thread_ts=thread_id,
            username="Dall-E",
            file="dall-e.png",
            title="respuesta"
        )
    def chatGPT(self, text, thread_id):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        answer = response["choices"][0]["text"]
        self.slack_web_client.chat_postMessage(
            channel=self.slack_chat_gpt_channel_id,
            username="chatGPT",
            text=answer,
            limit=4000,
            thread_ts=thread_id,
        )
