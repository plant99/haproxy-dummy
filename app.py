from flask import Flask

app = Flask(__name__)
import os

@app.route('/')
def hello_world():
    return 'Hello, World!' + os.system("hostname") 

app.run('0.0.0.0',5000)


