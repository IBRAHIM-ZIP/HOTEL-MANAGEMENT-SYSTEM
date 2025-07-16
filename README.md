# 🏨 Hotel Management System

A comprehensive Python-based hotel management system with MySQL database integration for managing staff, restaurant operations, customer bookings, and orders.

## ✨ Features

### 👨‍💼 Admin Management
- **Staff Management**: Add, view, update, and remove hotel staff
- **Restaurant Management**: Complete menu management with item operations
- **Customer Booking Management**: Handle room reservations and bookings
- **Order Management**: Process restaurant orders and track table service
- **ROOM MANAGEMENT**:ADD, Able to view available room
- **Feedback System**: Collect and manage customer feedback

### 🏪 Restaurant Operations
- Menu viewing and management
- Order processing with table number tracking
- Quantity updates and order cancellation
- Price calculations and total billing

### 🛏️ Booking System
- Room reservation management
- Check-in/check-out date tracking
- Room type selection
- Customer information storage
- Price calculation based on stay duration

### 🚪 Room Management System
- Manage the availability of rooms in the hotel
- Add new rooms to the hotel's inventory
- View which rooms are available, occupied, or under maintenance
- Update the status of any room (available, occupied, maintenance)
- Assign rooms to customer bookings automatically or manually
- Manage different room types and their rates

## 🛠️ Technical Stack

- **Language**: Python 3.x
- **Database**: MySQL
- **Libraries**: 
  - `pymysql` - MySQL database connectivity
  - `tabulate` - Table formatting for better display

## 📋 Prerequisites

Before running the application, ensure you have:

1. **Python 3.x** installed
2. **MySQL Server** running
3. Required Python packages:
   ```bash
   pip install pymysql tabulate
   ```

## 🗄️ Database Setup

### Database Schema

The system uses the following tables:

#### 1. EMPLOYES (Staff Management)
```sql
CREATE TABLE EMPLOYES (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100),
    DUTY VARCHAR(100),
    DATE_OF_JOIN DATE,
    GENDER VARCHAR(10),
    SHIFT VARCHAR(10),
    SALARY INT
);
```

#### 2. MENU (Restaurant Management)
```sql
CREATE TABLE MENU (
    DISH_ID INT AUTO_INCREMENT PRIMARY KEY,
    DISH_NAME VARCHAR(100),
    PRICE DECIMAL(10,2),
    STATUS VARCHAR(20) DEFAULT 'AVAILABLE'
);
```

#### 3. ORDERS (Order Management)
```sql
CREATE TABLE ORDERS (
    ORDER_ID INT AUTO_INCREMENT PRIMARY KEY,
    DISH_ID INT,
    DISH_NAME VARCHAR(100),
    STATUS VARCHAR(20),
    PRICE DECIMAL(10,2),
    QUANTITY INT,
    TOTAL_PRICE DECIMAL(10,2),
    TABLE_NUMBER INT
);
```

#### 4. BOOKING (Customer Booking)
```sql
CREATE TABLE BOOKING (
    BOOKING_ID INT PRIMARY KEY,
    USER_NAME VARCHAR(100),
    BOOKING_DAYS INT,
    PHONE_NO VARCHAR(10),
    CHECK_IN_DATE DATE,
    CHECK_OUT_DATE DATE,
    ROOM_TYPE VARCHAR(50),
    PRICE INT
);
```

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hotel-management-system.git
   cd hotel-management-system
   ```

2. **Install dependencies**:
   ```bash
   pip install pymysql tabulate
   ```

3. **Database Configuration**:
   - Create a MySQL database named `hotelmanagementproject`
   - Update the database connection details in the code:
   ```python
   b=a.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="hotelmanagementproject")
   ```

4. **Create database tables** using the SQL schema provided above

5. **Run the application**:
   ```bash
   python hotel_management.py
   ```

## 🚀 Usage

### Admin Access
- **Username**: `ibrahim khan`
- **Password**: `admin123`

### Main Menu Options
1. **Admin**: Full system access with management capabilities
2. **Customer**: Limited access for bookings and orders
3. **Staff**: Staff-specific operations
4. **Exit**: Close the application

### Admin Functions

#### Staff Management
- View all staff members
- Add new employees
- Remove staff members
- Update staff information (name, duty, salary, etc.)

#### Restaurant Management
- View menu items
- Add new dishes
- Delete menu items
- Update prices and availability
- Process orders by table number

#### Booking Management
- View all bookings
- Create new reservations
- Cancel bookings
- Update booking details

## 📊 Features Overview

### 🔐 Security Features
- Admin authentication system
- Input validation for phone numbers
- Booking ID constraints (1-1000 range)

### 💰 Financial Management
- Automatic price calculation for bookings
- Order total calculations
- Salary management for staff

### 📱 User-Friendly Interface
- Formatted table displays using `tabulate`
- Clear menu navigation
- Success/error message indicators
- Interactive prompts for user input

## 🔧 Code Structure

```
hotel_management.py
├── Database Connection Setup
├── Staff Management Functions
│   ├── view_staff()
│   ├── HIRE_STAFF()
│   ├── REMOVE_STAFF()
│   └── UPDATE_IN_STAFF()
├── Restaurant Management Functions
│   ├── view_menu()
│   ├── ADD_ITEMS_IN_MENU()
│   ├── DELETE_ITEMS_IN_MENU()
│   └── UPDATE_MENU_ITEMS()
├── Order Management Functions
│   ├── view_order()
│   ├── order()
│   ├── cancel_order()
│   └── update_order_quantity()
├── Booking Management Functions
│   ├── view_booking()
│   ├── add_booking()
│   ├── cancel_booking()
│   └── update_booking()
|
|__FEEDBACK MANAGEMENT FUNCTION()

|
└── Main Application Loop
```

## 📝 Sample Data

You can populate the database with sample data:

```sql
-- Sample staff data
INSERT INTO EMPLOYES (NAME, DUTY, DATE_OF_JOIN, GENDER, SHIFT, SALARY) VALUES
('John Doe', 'Manager', '2023-01-15', 'Male', 'Day', 50000),
('Jane Smith', 'Receptionist', '2023-02-01', 'Female', 'Day', 30000);

-- Sample menu data
INSERT INTO MENU (DISH_NAME, PRICE) VALUES
('Chicken Biryani', 250.00),
('Vegetable Curry', 180.00),
('Naan Bread', 50.00);
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Email: your.email@example.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] Web-based interface using Flask/Django
- [ ] Customer login system
- [ ] Payment integration
- [ ] Inventory management
- [ ] Reporting and analytics
- [ ] Email notifications
- [ ] Mobile app integration

## 🙏 Acknowledgments

- Thanks to the Python community for excellent libraries
- MySQL for reliable database management
- Contributors and testers

---

**⭐ Star this repository if you find it helpful!**