from tabulate import tabulate
import pymysql as  a 
b=a.connect (host="localhost",  user="root",  password="Azra@9758547293",  database="hotelmanagementproject")
print(F"CONNECTED SUCCESSFULLY TO THE DATABASE")
c=b.cursor()
print(F"\n")

#coding for admin
print("**********WELCOME TO THE HOTEL SYSTEM***********")
print("1.ADMIN")
print("2.customer")
print("3.staff")
print("4.exit")
choice=int(input("ENTER YOUR CHOICE: "))

if choice==1:
    while True:
        print("\n")
        print("1.Login as admin")
        print("2.register as admin")
        print("3.exit")
        print("\n")
        admin_choice=int(input("ENTER YOUR CHOICE: "))
        
        if admin_choice==1:
            username=input("ENTER YOUR USERNAME: ")
            password=input("ENTER YOUR PASSWORD: ")
            if username.lower() =="ibrahim khan" and password=="admin123":                               
                while True:
                    print("\n")
                    print()
                    print("************WELCOME TO ADMIN SECTION************")
                    print("1.STAFF MANAGEMENT")
                    print("2.RESTURANT MANAGEMENT")
                    print("3.CUSTOMER MANAGEMENT")
                    print("4.ROOM MANGEMENT")
                    print("5.FEEDBACKS")
                    print("6.exit")
                    admin_choice2=int(input("ENTER YOUR CHOICE: "))
                
                    if admin_choice2==1:
                        while True:
                            print("\n")
                            print("\n")
                            print("1.VIEW STAFF")
                            print("2.ADD STAFF")
                            print("3.DELETE STAFF")
                            print("4.select staff baised on condition")
                            print("5.exit")
                            enter_choice=int(input("ENTER YOUR CHOICE: "))
                    
                            if enter_choice==1:
                            
                                c.execute("select*from employes")
                                data=c.fetchall()
                                headers=[i[0] for i in c.description]
                                print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
                            
                                
                            elif enter_choice==2:
                                print("HOW MANY EMPLOYERS YOU WANT TO HIRE?")
                                a=int(input("ENTER A NUMBER OF EMPLOYERS YOU WANT TO HIRE: "))
                                for i in range(1,a+1):
                                    NAME=input("ENTER A NAME: ")
                                    DUTY=input("ENTER A DUTY: ")
                                    DATE_OF_JOIN=input("ENTER DATE IN YYYY-MM-DD FORMAT KINDLY: ")
                                    GENDER=input("ENTER A GENDER: ")
                                    SHIFT=input("ENTER A SHIFT DAY OR NIGHT: ")
                                    SALARY=int(input("ENTER A SALARY: "))
                                    QUERY="""INSERT INTO EMPLOYES(NAME,DUTY, DATE_OF_JOIN,GENDER,SHIFT,SALARY) 
                                           VALUES(%s,%s,%s,%s,%s,%s)"""
                                    value=(NAME,DUTY,DATE_OF_JOIN,GENDER,SHIFT,SALARY,)
                                    c.execute(QUERY,value)
                                    b.commit()
                                    print("✅ EMPLOYEE ADDED SUCCESSFULLY" )

                            elif enter_choice==3:
                                print("HOW MANY MEMBERS DO YOU WANT TO REMOVE FROM STAFF?")
                                a=int(input("ENTER A NUMBER OF  STAFF MEMBER YOU WANT TO REMOVE: "))
                                for i in range(1,a+1):
                                    NAME=input("ENTER THE NAME OF MEMBER: ")
                                    query="""select*from employes where NAME=(%s)"""
                                    VALUE=(NAME)
                                    c.execute(query,VALUE)
                                    data=c.fetchall()
                                    headers=[i[0] for i in c.description]
                                    print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
                                    ID=int(input("ENTER THE Id OF THE EMPLOYES: "))
                                    QUERY="""DELETE FROM EMPLOYES WHERE NAME=(%s) and ID=(%s)"""
                                    VALUE=(NAME,ID)
                                    c.execute(QUERY,VALUE)
                                    b.commit()
                                    
                                print("✅ REMOVE SUCCESSFULLY")

                            elif enter_choice==4:
                                print("1.select staff by name")
                                print("2.select staff by duty")
                                print("3.select staff by Id")
                                print("4.select staff                             
                            