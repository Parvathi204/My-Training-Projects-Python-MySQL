# 🏦 Project 3 – Banking System (Python + MySQL)

Welcome to the **Banking System**, a Python-based simulation of real-world bank operations integrated with MySQL. This project allows you to **create accounts, manage funds, and track transactions**—all from a simple, menu-driven interface.  

Designed for learning and demonstration purposes, this system provides a hands-on experience of **financial data management, database integration, and backend logic**, making it ideal for students, beginners, and enthusiasts exploring Python and MySQL.

---

## 🌟 Key Features

### 🏛 1. Create Account
- Open a new bank account by entering:
  - **Customer Name**  
  - **Account Type** (Savings/Current)  
  - **Initial Deposit**  
- Each account receives a **unique Account Number** for easy identification.  
- Records are stored securely in MySQL, ensuring permanent and organized storage.  
- Perfect for simulating real banking operations in a controlled environment.

---

### 💰 2. Deposit Money
- Add funds to an existing account seamlessly.  
- Steps involved:
  - Enter **Account Number**  
  - Enter **Deposit Amount**  
- Updates account balance in real-time.  
- Each deposit is recorded in the **transaction history** for accountability.  

---

### 🏧 3. Withdraw Money
- Withdraw money from your account securely.  
- Checks are performed to ensure **sufficient balance** before withdrawal.  
- The withdrawal is recorded in the **transaction log**, maintaining financial accuracy.  
- Mimics real-world ATM or teller operations.

---

### 📋 4. View Balance
- Quickly check the current balance of any account.  
- Helps users monitor their funds and validate deposits or withdrawals.  
- Ensures transparency and easy verification of account status.

---

### 📝 5. Transaction History
- Every deposit and withdrawal is logged with:
  - **Account Number**  
  - **Transaction Type** (Deposit/Withdrawal)  
  - **Amount**  
  - **Date & Time**  
- Provides a complete **financial activity overview**, similar to real bank statements.  
- Essential for audits, verification, and financial tracking.

---

## 🗄 Database Integration (MySQL)
The system uses MySQL to store accounts and transaction details for **reliability and permanence**.  

### **Tables Used**
1. **accounts**
   - `account_no` – Primary Key  
   - `name` – Customer Name  
   - `acc_type` – Account Type  
   - `balance` – Current Balance  

2. **transactions**
   - `trans_id` – Primary Key, Auto Increment  
   - `account_no` – Foreign Key (linked to accounts)  
   - `type` – Deposit/Withdrawal  
   - `amount` – Transaction Amount  
   - `date_time` – Timestamp  

**Benefits of MySQL Integration:**
- Efficient and secure **CRUD operations**  
- Structured data organization  
- Easy retrieval of account and transaction details  
- Real-time balance updates  

Python interacts with MySQL using **mysql-connector-python**, ensuring smooth and reliable database communication.

---

## 🎯 Purpose of the Project
The Banking System is designed to:
- Simulate realistic bank operations in a controlled environment  
- Provide hands-on experience with Python and MySQL  
- Teach **CRUD operations, data integrity, and transaction tracking**  
- Strengthen understanding of backend logic and database relationships  
- Offer a mini-project suitable for academic submission, portfolio, or learning

It’s a practical tool for understanding **how financial systems work** at a basic level and for building confidence in programming with databases.

---

## ⚙️ Technologies Used
- **Python 3** – Core language for development  
- **MySQL (XAMPP/phpMyAdmin)** – Database management  
- **mysql-connector-python** – Python-MySQL connector  
- **Visual Studio Code** – Development IDE  

---

## 🧑‍💻 Ideal For
- Students learning **Python + MySQL integration**  
- Beginners exploring backend development  
- Academic mini-project submissions  
- Anyone wanting a **realistic banking simulation**  

---

**Manage accounts, track transactions, and experience banking logic like a pro!**

