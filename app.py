#FLASK_APP=app.py flask run
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask"

    #this will start the application
    if __name__=="__main__":
        app.run()


#Testing app