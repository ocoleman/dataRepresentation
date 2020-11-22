from flask import Flask, url_for, request, abort, redirect

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    #return "Hello World"
    return redirect(url_for('login')) #redirected to /login

#abort
@app.route('/login')
def login():
    abort(401)
    return "served by Login"


#get method
@app.route('/user')
def getUSer():
    return "served by getUser"

#passing variables through url
@app.route('/user/<int:id>')
def findByIdUser(id):
    return "served by findByIdUser with id = "+str(id)
#post method curl -X POST url
@app.route('/user', methods=['POST'])
def createUser():
    return "served by createUser"

@app.route("/demo_url_for")
def demoUrlFor():
    returnString = "url for index= "+url_for('index')
    returnString += "<br/>"
    returnString += "url for findByIdUser= " +url_for('findByIdUser', id=12)
    return returnString

#returns the method
@app.route("/demo_request", methods=['POST', 'GET', 'DELETE'])
def demoRequest():
    return request.method

if __name__ == "__main__":
    print("in if")
    app.run() #allows for realtime editing