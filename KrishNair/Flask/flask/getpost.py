from flask import Flask,render_template,request


#initialize the app 
#Creates an instance of Flask Class which will be your WSGI(Web Server Gateway interface) application.
###WSGI application 
app = Flask(__name__)

#Routing
@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask Course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello eddesh {name}!'
    return render_template('form.html')

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
    app.run(debug=True)