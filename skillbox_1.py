from flask import Flask, render_template, request
from datetime import datetime
import json


app = Flask(__name__)

DB_FILE = "./data/db.json"
db = open(DB_FILE, "r")  # Открываем файл для чтения
data = json.load(db)  # Загрузить все данные в формате JSON из файла
messages = data["messages"]  # Из полученных данных берем поле messages


def add_message(text, sender):
    now = datetime.now()
    new_message = {
        "text": text,
        "sender": sender,
        "time": now.strftime("%Y-%m-%d %H:%M")
    }
    messages.append(new_message)


def print_message(message):
    print(f"[{message['sender']}]: {message['text']} / {message['time']}")


@app.route("/")
def index_page():
    return "Hello, Skillchat2022 welcomes you"


@app.route("/get_messages")
def get_messages():
    result = {"messages": messages}
    return result


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/send_message")
def send_message():
    name = request.args["name"]
    text = request.args["text"]
    add_message(text, name)
    return "OK"


app.run()
