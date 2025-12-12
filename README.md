# 🏥 Project 6 – Hospital Patient Record System (Python + MySQL)

Welcome to the **Hospital Patient Record System**, a Python-based application integrated with MySQL that helps manage patient information efficiently. This system allows healthcare administrators to **add, update, delete, and search patient records**, as well as **track admission and discharge status** — all through an easy-to-use, menu-driven interface.  

Designed for learning and demonstration purposes, this system provides hands-on experience in **healthcare data management, database integration, and backend logic**, making it perfect for academic projects or beginners exploring Python and MySQL.

---

## 🌟 Key Features

### 📝 1. Add New Patient Record
- Register a new patient by entering:
  - **Patient Name**  
  - **Age**  
  - **Medical Condition / Diagnosis**  
  - **Admission Status** (Admitted / Not Admitted)  
- All details are stored securely in the MySQL database.  
- Ensures structured storage for efficient patient management.

---

### 🏥 2. Update Patient Details
- Modify patient information using the **Patient ID**:  
  - Update **name, age, gender, diagnosis**, or **admission/discharge status**  
- Helps maintain accurate and up-to-date medical records.  
- Supports real-time updates for hospital staff.

---

### ❌ 3. Delete Patient Record
- Permanently remove outdated or discharged patient records using **Patient ID**.  
- Keeps the database clean and relevant.  
- Ensures proper management of patient data.

---

### 🔍 4. Search Patient by Name or ID
- Quickly locate a patient using:
  - **Patient ID**  
  - **Patient Name**  
- Useful for verifying patient details, updating records, or monitoring treatment progress.

---

### 📋 5. View All Patient Records
- Retrieve a complete list of all patients in the hospital, including:
  - **Patient ID**  
  - **Name**  
  - **Age**   
  - **Diagnosis**  
  - **Admission / Discharge Status**  
- Provides a comprehensive overview of hospital patients for administrators.

---

### 🏥 6. Track Admission & Discharge Status
- Monitor which patients are currently admitted and which have been discharged.  
- Update the status easily when a patient is admitted or discharged.  
- Ensures efficient **hospital bed management and patient flow tracking**.

---

## 🗄 Database Integration (MySQL)
The system uses MySQL for storing patient records securely and efficiently.

### **Tables Used**
1. **patients**
   - `patient_id` – Primary Key, Auto Increment  
   - `name` – Patient Name  
   - `age` – Patient Age  
   - `diagnosis` – Medical Condition  
   - `status` – Admission / Discharge Status  

**Benefits of MySQL Integration:**
- Reliable and structured storage of patient data  
- Efficient **CRUD operations** for patient management  
- Easy retrieval of records for search and reporting  
- Real-time updates for admission and discharge tracking  

Python interacts with MySQL using **mysql-connector-python**, ensuring smooth database operations and real-time record management.

---

## 🎯 Purpose of the Project
The Hospital Patient Record System aims to:
- Digitize patient management and hospital operations  
- Track admissions, discharges, and medical records efficiently  
- Maintain accurate and up-to-date patient information  
- Teach **Python + MySQL CRUD operations** in a real-world healthcare scenario  
- Provide a mini-project suitable for academic submission or portfolio building  

It’s a practical example of **how hospitals manage patient data**, helping students understand database-driven application development in healthcare.

---

## ⚙️ Technologies Used
- **Python 3** – Core programming language  
- **MySQL (XAMPP/phpMyAdmin)** – Database management  
- **mysql-connector-python** – Python-MySQL connector  
- **Visual Studio Code** – Development IDE  

---

## 🧑‍💻 Ideal For
- Students learning Python + MySQL integration  
- Beginners exploring healthcare management systems  
- Academic mini-projects or portfolio demonstrations  
- Anyone interested in hospital data management simulations  

---

**Manage patient records, monitor admissions, and streamline hospital operations with this interactive Hospital Patient Record System!**
