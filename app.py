from flask import Flask
import time

app = Flask(__name__)

@app.route('/delay')
def delay():
    time.sleep(130)  # Simula un retraso de 130 segundos
    return "This is a delayed response"

