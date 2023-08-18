import json
import requests
import logging
from flask import Flask, request
from constant import *


app = Flask(__name__)

@app.route('/mesage_request', methods=['POST'])
def receive_json_file():
    try:
        data = request.json
        if not is_valid_key_token(data.get("token")):
            return "Invalid key Token.", 403
        fone_number = data.get('fone_number')
        message = data.get('message')

        if fone_number and message:
            send_telegram_message(fone_number, message)
            return 'Message has been sent to telegram.', 200
        else:
            return 'Incomplete Json Data.', 400
    except Exception as error:
        logging.error(str(error))
        return 'Error while processing Json', 500

def is_valid_key_token(key_token:str) -> bool:
    return key_token == VALID_KEY

def send_telegram_message(fone_number:str, message:str):
    telegram_url = TELEGRAM_URL.format(
                                    TELEGRAM_TOKEN = TELEGRAM_TOKEN,
                                    TELEGRAM_CHAT_ID = TELEGRAM_CHAT_ID,
                                    fone_number = fone_number,
                                    message = message
                                        )
    response = requests.get(telegram_url)
    response.raise_for_status()

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)