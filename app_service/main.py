import json
import requests
import logging
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""

@app.route('/mesage_request', methods=['POST'])
def receive_json_file():
    try:
        data = request.json
        fone_number = data.get('fone_number')
        message = data.get('message')

        if fone_number and message:
            send_telegram_message(fone_number, message)
        else:
            return 'Incomplete Json Data.', 400
    except Exception as error:
        logging.error(str(error))
        return 'Error while processing Json', 500

def send_telegram_message(fone_number, message):
    pass

if __name__=='__main__':
    app.run()