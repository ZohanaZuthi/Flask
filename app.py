# flask app url routing
from flask import Flask

app=Flask(__name__)

    
    
@app.route("/",methods=["GET"])
def welcome():
    return "Welcome to my flask tutorial"

@app.route("/index",methods=['GET'])
def index():
    return "it is index page"


if __name__=="__main__":
    app.run(debug=True)
