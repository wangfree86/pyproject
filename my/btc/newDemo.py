from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '您好，欢迎来到我的虚拟货币交易所!'