from flask import Flask, request, jsonify
from flask_cors import CORS   # ✅ add this

app = Flask(__name__)
CORS(app)  

acc_created=False
acc_balance=0

@app.route("/create",methods=['POST'])
def create():
    global acc_balance,acc_created
    if not acc_created:
        acc_created=True
        acc_balance=0
        return jsonify({"message":"Account created successfully"})
    return jsonify({"message": "Account already exists!"})
    
@app.route("/balance")
def get_balance():
    if not acc_created:
        return jsonify({"messsage":"Create a account first"})
    return jsonify({"message":f"balance is {acc_balance}"})

@app.route("/deposit", methods=["POST"])
def deposit():
    global acc_balance
    amount = int(request.json["amount"])
    acc_balance += amount
    return jsonify({"message": f"New balance: {acc_balance}"})

@app.route("/withdraw", methods=["POST"])
def withdraw():
    global acc_balance
    amount = int(request.json["amount"])
    if amount > acc_balance:
        return jsonify({"message": "Insufficient balance"})
    acc_balance -= amount
    return jsonify({"message": f"Remaining balance: {acc_balance}"})

app.run(debug=True)