# 🍽️ Project 5 – Online Order System (Python + MySQL)

Welcome to the **Online Order System**, a Python-based application integrated with MySQL that simulates a simple food or product ordering platform. This system allows users to **add menu items, place orders, track order history, and update payment status**, all through a straightforward menu-driven interface.  

Designed for learning and demonstration purposes, it provides practical experience in **order management, database integration, and backend logic**, making it ideal for academic projects, mini-projects, or beginners exploring Python and MySQL.

---

## 🌟 Key Features

### 📋 1. Add Items to Menu
- Add new products or food items to the menu by entering:
  - **Item Name**  
  - **Price**  
  - **Available Quantity**  
- Data is stored in the MySQL database for permanent, organized storage.  
- Keeps your menu up-to-date for smooth order processing.

---

### 🛒 2. Place Orders
- Place an order by selecting:
  - **Item Name or ID**  
  - **Quantity**  
  - **Customer Name**  
- The system automatically checks **stock availability** and updates quantities in real-time.  
- Each order is recorded in the database with a **unique Order ID**, ensuring proper tracking.

---

### 📝 3. Track Order History
- View all past orders with details such as:
  - **Order ID**  
  - **Customer Name**  
  - **Items Ordered**  
  - **Quantity**  
  - **Order Date & Time**  
- Helps administrators or shop owners monitor sales and customer preferences.  

---

### 💳 4. Update Payment Status
- Record payment status for each order:  
  - **Paid / Failed**  
- Provides a clear overview of completed and pending transactions.  
- Essential for financial tracking and accountability.

---

## 🗄 Database Integration (MySQL)
The system uses MySQL to store all menu items, orders, and payment details for **accuracy and reliability**.

### **Tables Used**
1. **menu_items**
   - `item_id` – Primary Key  
   - `name` – Item Name  
   - `price` – Item Price  
   - `quantity` – Available Quantity  

2. **orders**
   - `order_id` – Primary Key  
   - `customer_name` – Customer Name  
   - `item_id` – Foreign Key (linked to menu_items)  
   - `quantity` – Quantity Ordered  
   - `order_date` – Timestamp of Order  
   - `payment_status` – Paid / Failed  

**Benefits of MySQL Integration:**
- Secure, permanent storage of all orders and menu items  
- Real-time updates for stock and order processing  
- Structured, easily retrievable data for reports and management  
- Smooth Python-MySQL interaction via **mysql-connector-python**  

---

## 🎯 Purpose of the Project
The Online Order System is designed to:
- Digitize and streamline ordering processes  
- Track stock, orders, and payments efficiently  
- Teach **CRUD operations, order management, and database integration**  
- Provide hands-on experience with Python + MySQL for real-world applications  
- Serve as a mini-project for academic submissions or portfolio building  

It’s a practical example of **how online ordering platforms function**, suitable for small shops, food vendors, or learning projects.

---

## ⚙️ Technologies Used
- **Python 3** – Core language for development  
- **MySQL (XAMPP/phpMyAdmin)** – Backend database  
- **mysql-connector-python** – Python-MySQL connector  
- **Visual Studio Code** – Development IDE  

---

## 🧑‍💻 Ideal For
- Students practicing Python + MySQL integration  
- Beginners learning order management systems  
- Mini-project submissions and portfolios  
- Anyone wanting to understand **real-world online ordering systems**  

---

**Simplify ordering, track sales, and manage payments efficiently with this Online Order System!**

