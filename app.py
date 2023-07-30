import os
import requests as rq
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        name = request.form.get('name', 'Без имени')
        phone = request.form.get('phone', 'Без телефона')
        telegram = request.form.get('telegram', 'Без телеграмма')
        whatsapp = request.form.get('whatsapp', 'Без востапа')

        to_telegram = {
            'name': name,
            'phone': phone,
            'telegram': telegram,
            'whatsapp': whatsapp,
        }

        message = 'Внимание! Новая заявка!!!\n' \
                  f'Имя: {to_telegram.get("name")}\n' \
                  f'Телефон: {to_telegram.get("phone")}\n' \
                  f'Telegram: {to_telegram.get("telegram")}\n' \
                  f'WhatsApp: {to_telegram.get("whatsapp")}\n'


        url = f"https://api.telegram.org/bot{os.environ.get('vk_token')}" \
              f"/sendMessage?chat_id={os.environ.get('chat_id')}" \
              f"&text={message}"

        rq.get(url)


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)