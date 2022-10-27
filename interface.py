from flask import Flask ,render_template ,jsonify,request
import calculation
import config
#from calculation import get_addition

app  = Flask(__name__)
###########################################################################################
############################### Base API ##################################################
###########################################################################################
@app.route("/") # HOME API
def hello_flask():
    print("Welcome to flask")
    return render_template ("home.html")



###########################################################################################
############################### Test API ##################################################
###########################################################################################
@app.route("/test")
def test():
    print("*"*80)
    print("This is testing API")
    print("*"*80)
    return jsonify({"Message": "Successful"})


###########################################################################################
############################### Addition API ##################################################
###########################################################################################
@app.route("/addition")
def addition():
    input_data = request.form
    #print(input_data)
    a= int(input_data["a"])
    b= eval(input_data["b"])

    result = calculation.get_addition(a,b)
    return jsonify ({"Result" : f"addition of {a} and {b} is {result}"})
###########################################################################################
############################### Multiplication API ##################################################
###########################################################################################
@app.route("/multiplication")

def multi():
    data = request.get_json()
    print("Data is :",data)
    a = eval(data["a"])
    b = eval(data["b"])
    print("")
    result = calculation.get_multiplication(a,b)
    return jsonify({"Result" : f"multiplication of {a} and {b} is {result}"})





if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug = True)