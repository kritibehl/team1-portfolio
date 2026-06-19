import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Henrique", url=os.getenv("URL"), photo="henrique.jpg", switch_url="/kriti", switch_name="Kriti Behl")


@app.route('/henrique')
def henrique():
    return render_template('index.html', title="Henrique", url=os.getenv("URL"), photo="henrique.jpg", switch_url="/kriti", switch_name="Kriti Behl")


@app.route('/kriti')
def kriti():
    return render_template('index.html', title="Kriti Behl", url=os.getenv("URL"), photo="logo.jpg", switch_url="/henrique", switch_name="Henrique")
