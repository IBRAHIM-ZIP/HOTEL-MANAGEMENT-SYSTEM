import pymysql as a
try:
    connection = a.connect(host='localhost', user='root', password='Azra@9758547293', database='hotelmanagementproject')
    print("Connected to the database successfully")
except a.MySQLError:
    print("Failed to connect to the database")
y=connection.cursor()

#LETS WORK AS A START 

print("Welcome to the Hotel SONA MANAGEMENT SYSTEM")
print("1. ADMIN")
print("2. STAFF OR COUSTOMER")
choice = int(input("Enter your choice: "))

if choice ==1:
    while True:
        print("1. Login as Admin")
        print("2. Register as Admin")
        print("3. Exit")
        admin_choice = int(input("Enter your choice: "))
        
        if admin_choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            # Here you would typically check the credentials against a database
            if  password == "Azra@9758547293":
                # Assuming the credentials are correct
                print("Login successful!")
                break
            else:
                print("Invalid credentials, please try again.")
        elif admin_choice == 2:
            print("Registration functionality not implemented yet.")
        elif admin_choice == 3:
            print("Exiting...")
            exit()
        else:
            print("Invalid choice, please try again.")

    print("welcome to the admin section")
    print("1. staff management")
    print("2. customer management")
    print("3. room management")
    print("4. booking management")
    print("5.resturant management")
    print(".exit")
    admin_section_choice = int(input("Enter your choice: "))
    if admin_section_choice == 1:
        print("Welcome to the staff management section")
        print("1. Add staff")
        print("2. View staff")
        print("3. Update staff")
        print("4. Delete staff")
        staff_choice = int(input("Enter your choice: "))
        
        if staff_choice == 1:
            name = input("Enter staff name: ")
            duty = input("Enter staff duty: ")
            date_of_join = input("Enter date of join (YYYY-MM-DD): ")
