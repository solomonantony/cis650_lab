from flask import Flask, jsonify
app = Flask(__name__)  #create an instance of the Flask object using a speciap pytjon variable
myData = [{'Customer': 'ABC', 'Q1':200, 'Q2':230, 'Q3':300},
          {'Customer': 'XYZ', 'Q1':120, 'Q2':320, 'Q3':200}]

@app.route('/') #decorator registers the hello function to handle requests made to the root URL
@app.route('/hello') #decorator registers the hello function to handle requests made to the root URL
def hello():
    return "Hello, world!"
@app.route('/data', methods = ['GET'])
def getMyData():
    return jsonify({'myData':myData})

@app.route('/quarter/<quarter>')
def get_quarter_data(quarter):
    result = ''
    if quarter in ['Q1', 'Q2', 'Q3']:
        for data_line in myData:
            result = result + f'{data_line["Customer"]}: {data_line[quarter]}<br>'
        return result
    else:
        return "Invalid quarter number"
# create a decorator that will respond with all quarter data for a given customer
@app.route('/customer/<customer>')
def get_customer_data(customer):
    for customer_data in myData:
        if customer_data['Customer'] == customer:
            return jsonify(customer_data)
    return "Customer not found"    

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
