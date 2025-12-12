from flask import Flask, render_template, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="meenakshi"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.get_json()
    acc_no = data['account_number']
    name = data['name']
    balance = data['balance']

    cursor.execute(
        "INSERT INTO accounts (account_number, name, balance) VALUES (%s, %s, %s)",
        (acc_no, name, balance)
    )
    db.commit()
    return jsonify({"status": "success", "message": "Account Created Successfully!"})

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    acc_no = data['account_number']
    amount = float(data['amount'])

    cursor.execute("SELECT balance FROM accounts WHERE account_number=%s", (acc_no,))
    result = cursor.fetchone()
    if not result:
        return jsonify({"status": "error", "message": "Account Not Found!"})

    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s", (amount, acc_no))
    cursor.execute(
        "INSERT INTO transactions (account_number, type, amount, date) VALUES (%s, %s, %s, %s)",
        (acc_no, "Deposit", amount, datetime.now())
    )
    db.commit()
    return jsonify({"status": "success", "message": "Amount Deposited Successfully!"})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    acc_no = data['account_number']
    amount = float(data['amount'])

    cursor.execute("SELECT balance FROM accounts WHERE account_number=%s", (acc_no,))
    result = cursor.fetchone()
    if not result:
        return jsonify({"status": "error", "message": "Account Not Found!"})

    if amount > result[0]:
        return jsonify({"status": "error", "message": "Insufficient Balance!"})

    cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s", (amount, acc_no))
    cursor.execute(
        "INSERT INTO transactions (account_number, type, amount, date) VALUES (%s, %s, %s, %s)",
        (acc_no, "Withdraw", amount, datetime.now())
    )
    db.commit()
    return jsonify({"status": "success", "message": "Withdrawal Successful!"})

@app.route('/balance', methods=['POST'])
def balance():
    data = request.get_json()
    acc_no = data['account_number']
    cursor.execute("SELECT balance FROM accounts WHERE account_number=%s", (acc_no,))
    result = cursor.fetchone()
    if result:
        return jsonify({"status": "success", "balance": result[0]})
    else:
        return jsonify({"status": "error", "message": "Account Not Found!"})

@app.route('/transactions', methods=['POST'])
def transactions():
    data = request.get_json()
    acc_no = data['account_number']
    cursor.execute("SELECT type, amount, date FROM transactions WHERE account_number=%s", (acc_no,))
    rows = cursor.fetchall()
    if rows:
        history = [{"type": t[0], "amount": t[1], "date": str(t[2])} for t in rows]
        return jsonify({"status": "success", "transactions": history})
    else:
        return jsonify({"status": "error", "message": "No Transactions Found"})

if __name__ == '__main__':
    app.run(debug=True)
