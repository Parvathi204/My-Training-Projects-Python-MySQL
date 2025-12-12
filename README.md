# 📚 Project 4 – Library Management System (Python + MySQL)

Welcome to the **Library Management System**, a Python-based application integrated with MySQL to manage books and library users efficiently. This system allows librarians or administrators to **add, update, delete books, register users, issue and return books**, and view all issued books — all through a simple menu-driven interface.  

It’s designed to simulate real-world library operations, providing hands-on experience in **data management, database integration, and backend logic**, making it perfect for academic projects or learning exercises.

---

## 🌟 Key Features

### 📖 1. Add / Update / Delete Books
- **Add Books:** Enter book details such as:
  - **Book Title**  
  - **Author**  
  - **Quantity Available**  
- **Update Books:** Modify existing book details using the **Book ID**.  
- **Delete Books:** Remove books from the system if they are outdated or unavailable.  
- Ensures accurate and up-to-date book records in the library database.

---

### 👥 2. Register Users
- Register new library users by collecting:
  - **User Name**  
  - **User ID / Membership ID**  
  - **Contact Information**  
- Keeps a structured record of all library members.  
- Supports issuing books and tracking borrowings efficiently.

---

### 📚 3. Issue / Return Books
- **Issue Books:** Assign books to registered users by entering:
  - **User ID**  
  - **Book ID**  
- Automatically updates book availability in the database.  
- **Return Books:** When books are returned:
  - Updates inventory  
  - Records return date  
- Ensures accurate tracking of which user has which book at any time.

---

### 📝 4. View Issued Books
- Retrieve a list of all currently issued books along with:
  - **Book ID**  
  - **Book Title**  
  - **User ID / Name**  
  - **Issue Date**  
- Helps librarians monitor borrowed books and due dates efficiently.

---

## 🗄 Database Integration (MySQL)
The system uses MySQL for storing all book and user information securely and reliably.  

### **Tables Used**
1. **books**
   - `book_id` – Primary Key  
   - `title` – Book Title  
   - `author` – Author Name  
   - `quantity` – Number of Copies Available  

2. **users**
   - `user_id` – Primary Key  
   - `name` – User Name  
   - `contact` – Contact Information  

3. **issued_books**
   - `issue_id` – Primary Key  
   - `book_id` – Foreign Key (linked to books)  
   - `user_id` – Foreign Key (linked to users)  
   - `issue_date` – Date Book Was Issued  
   - `return_date` – Date Book Was Returned  

**Benefits of MySQL Integration:**
- Secure and persistent storage for books and users  
- Efficient **CRUD operations** for library management  
- Real-time updates on issued and available books  
- Structured organization and easy retrieval of records  

Python interacts with MySQL using **mysql-connector-python**, providing smooth database operations.

---

## 🎯 Purpose of the Project
The Library Management System aims to:
- Digitize library operations for easy management  
- Track books and users efficiently  
- Automate book issuing and returning  
- Maintain accurate and up-to-date records  
- Teach **Python and MySQL CRUD operations** and backend logic  

It’s a practical project for students, providing a real-world example of how libraries manage inventory and user data.

---

## ⚙️ Technologies Used
- **Python 3** – Core programming language  
- **MySQL (XAMPP/phpMyAdmin)** – Backend database  
- **mysql-connector-python** – Python-MySQL connector  
- **Visual Studio Code** – Development IDE  

---

## 🧑‍💻 Ideal For
- Students learning Python + MySQL integration  
- Academic mini-projects or portfolio building  
- Beginners practicing CRUD operations  
- Anyone interested in real-world library management simulations  

---

**Effortlessly manage books, users, and borrowing records with this interactive Library Management System!**

