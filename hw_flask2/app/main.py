from flask import Flask
from random import randint

from flask import Flask

app = Flask(__name__)

@app.route('/')
def random_num():
    num = randint(1, 1000+1)
    num = str(num)
    return num
