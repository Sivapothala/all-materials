from flask import Flask


#initialize the app 
#Creates an instance of Flask Class which will be your WSGI(Web Server Gateway interface) application.
###WSGI application 
app = Flask(__name__)

#Routing
@app.route("/")
def welcome():
    return "Welcome to Flask Course"


#Entry Point for a .py file
if __name__ == "__main__":
    '''
    (method) def run(
    host: str | None = None, #we can define the host
    port: int | None = None, 
    debug: bool | None = None, #if true no need to restart the app to see the changes #Automatic restart    
    load_dotenv: bool = True,
    **options: Any
) -> None
    '''
    app.run()