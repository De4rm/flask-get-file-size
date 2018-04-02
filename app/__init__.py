from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "hi i am new secret key"

from app import routes