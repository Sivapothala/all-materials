from flask import Flask


#initialize the app 
#Creates an instance of Flask Class which will be your WSGI(Web Server Gateway interface) application.
###WSGI application 
app = Flask(__name__)

#Routing
@app.route("/",methods=['GET'])
def welcome():
    return "Welcome to Flask Course"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)