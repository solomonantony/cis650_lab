from flask import Flask, jsonify
app = Flask(__name__)  #create an instance of the Flask object using a speciap pytjon variable
@app.route('/') #decorator registers the hello function to handle requests made to the root URL
@app.route('/hello') #decorator registers the hello function to handle requests made to the root URL
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
