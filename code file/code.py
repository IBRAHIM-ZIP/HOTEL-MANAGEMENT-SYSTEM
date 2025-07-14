from tabulate import tabulate
import pymysql as  a 
b=a.connect (host="localhost",  user="root",  password="Azra@9758547293",  database="hotelmanagementproject")
print(F"CONNECTED SUCCESSFULLY TO THE DATABASE {b.get_server_info()}")
c=b.cursor()
print()


#✨✨✨✨✨✨✨✨✨✨✨✨✨✨function required to make for ADMIN✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨ 
#------------------------------------------------------------------------------------------------------------------
#➡️FOR STAFF MANAGEMENT


def view_staff():
    q="select*from employes"
    c.execute(q)
    data=c.fetchall()
    headers=[i[0] for i in c.description]
    print(tabulate(data,headers=headers,tablefmt="fancy_grid"))

def REMOVE_STAFF(): 
    print()
    print("HOW MANY MEMBERS YOU WANT TO DELETE")
    print("1.WANT TO DELETE ALL MEMBER ?")
    print("2.WANT TO DELETE FEW MEMBERS?")
    print()
    X=int(input("ENTER YOUR CHOICE: "))
    if X==1:
        query="""DELETE FROM EMPLOYES"""
        c.execute(query)
        b.commit()
        print("✅ REMOVE SUCCESSFULLY")
    elif X==2:
        print("HOW MANY YOU WANT TO DELETE?")
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
            
    else:
        print("INVALID CHOICE!!| choose wisely|")
        
        
        
        
        
    


#function for adding in the table

def HIRE_STAFF():
    print("HOW MANY EMPLOYERS YOU WANT TO HIRE?")
    a=int(input("ENTER A NUMBER OF EMPLOYERS YOU WANT TO HIRE: "))
    for i in range(1,a+1):
        print()
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
        
        
        
    
          
          
def UPDATE_IN_STAFF():
    print("😍 WANNA UPDATE SOME THING?")
    print("❌ID IS PERMANENT IT CANT BE CHANGED❌")
    print("1.NAME")
    print("2.DUTY")
    print("3.DATE_OF_JOIN")
    print("4.GENDER")
    print("5.SALARY")
    print("6.SHIFT")
    print(f"/n /n")
    A=int(input("ENTER YOUR CHOICE: "))
    if A==1:
        NAME=input("ENTER THE WRONG NAME: ")
        query="""select*from employes where NAME=(%s)"""
        VALUE=(NAME,)
        c.execute(query,VALUE)
        data=c.fetchall()
        headers=[i[0] for i in c.description]
        print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
        
        X=input("ENTER THE NAME YOU WANT TO REPLACE")
        Id=int(input("ENTER A Id :"))
        query="""UPDATE EMPLOYES
                    SET NAME=%s
                    where NAME=%s and Id=%s"""
        VALUES=(X,NAME,Id) 
        c.execute(query,VALUES)
        b.commit()
        print("✅DONE")
    
    
    elif A==2:
        DUTY=input("ENTER THE OLD DUTY : ")
        NAME=input("ENTER YOUR NAME: ")
        query="""select*from employes where NAME=(%s)"""
        VALUE=(NAME,)
        c.execute(query,VALUE)
        data=c.fetchall()
        headers=[i[0] for i in c.description]
        print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
        Id=int(input("ENTER THE ID: "))
        
        NEW_DUTY=input("ENTER NEW DUTY: ")
        QUERY="""UPDATE EMPLOYES 
                 SET DUTY=%s
                 where NAME=%s and Id=%s"""
        values=(NEW_DUTY,NAME,Id)
        c.execute(QUERY,values)
        b.commit()
        print("✅DONE")
    elif A==3:
        DATE_OF_JOIN=input("ENTER THE DATE_OF_JOIN : ")
        NAME=input("ENTER YOUR NAME: ")
        query="""select*from employes where NAME=(%s)"""
        VALUE=(NAME,)
        c.execute(query,VALUE)
        data=c.fetchall()
        headers=[i[0] for i in c.description]
        print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
        Id=int(input("ENTER THE ID: "))
        
        NEW_DATE_OF_JOIN=input("ENTER NEW DATE IN YYYY-MM-DD FORMAT: ")
        QUERY="""UPDATE EMPLOYES 
                 SET DATE_OF_JOIN=%s
                 where NAME=%s and Id=%s"""
        values=(NEW_DATE_OF_JOIN,NAME,Id)
        c.execute(QUERY,values)
        b.commit()
        print("✅DONE")
    elif A==4:
        GENDER=input("ENTER THE OLD GENDER : ")
        NAME=input("ENTER YOUR NAME: ")
        query="""select*from employes where NAME=(%s)"""
        VALUE=(NAME,)
        c.execute(query,VALUE)
        data=c.fetchall()
        headers=[i[0] for i in c.description]
        print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
        Id=int(input("ENTER THE ID: "))
        
        NEW_GENDER=input("ENTER CORRECT GENDER: ")
        QUERY="""UPDATE EMPLOYES 
                 SET GENDER=%s
                 where NAME=%s and Id=%s"""
        values=(NEW_GENDER,NAME,Id)
        c.execute(QUERY,values)
        b.commit()
        print("✅DONE")
    elif A==5:
        NAME=input("ENTER YOUR NAME: ")
        query="""select*from employes where NAME=(%s)"""
        VALUE=(NAME,)
        c.execute(query,VALUE)
        data=c.fetchall()
        headers=[i[0] for i in c.description]
        print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
        Id=int(input("ENTER THE ID: "))
        
        UPDATED_SALARY=int(input("ENTER NEW salary: "))
        QUERY="""UPDATE EMPLOYES 
                 SET salary=%s
                 where NAME=%s and Id=%s"""
        values=(UPDATED_SALARY,NAME,Id)
        c.execute(QUERY,values)
        b.commit()
        print("✅DONE")
    elif A==6:
        shift=input("ENTER THE OLD shift : ")
        NAME=input("ENTER YOUR NAME: ")
        query="""select*from employes where NAME=(%s)"""
        VALUE=(NAME,)
        c.execute(query,VALUE)
        data=c.fetchall()
        headers=[i[0] for i in c.description]
        print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
        Id=int(input("ENTER THE ID: "))
        
        NEW_SHIFT=input("ENTER NEW shift: ")
        QUERY="""UPDATE EMPLOYES 
                 SET SHIFT=%s
                 where NAME=%s and Id=%s"""
        values=(NEW_SHIFT,NAME,Id)
        c.execute(QUERY,values)
        b.commit()
        print("✅DONE")
    else:
        print("invalid selection")
        
          
#------------------------------------------------------------------------------------------------------#         
#➡️➡️FUNCTION FOR RESTURANT 

def view_menu():
    c.execute("select*from menu")
    data=c.fetchall()
    headers=[i[0] for i in c.description]
    print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
                                



def DELETE_ITEMS_IN_MENU():
    print("HOW MANY ITEMS YOU WANT TO DELETE")
    print("1.WANT TO DELETE ALL ITEMS ?")
    print("2.WANT TO DELETE FEW ITEMS?")
    print()
    X=int(input("ENTER YOUR CHOICE: "))
    if X==1:
        query="""DELETE FROM  menu"""
        c.execute(query)
        b.commit()
        print("✅ REMOVE SUCCESSFULLY AND AUTO-INCREMENT RESET")
    elif X==2:
        print("HOW MANY YOU WANT TO DELETE?")
        a=int(input("ENTER A NUMBER OF ITEMS YOU WANT TO REMOVE: "))
        for i in range(1,a+1):
            DISH_NAME=input("ENTER THE NAME OF ITEM: ")
            query="""select*from menu where DISH_NAME=(%s)"""
            VALUE=(DISH_NAME,)
            c.execute(query,VALUE)
            data=c.fetchall()
            headers=[i[0] for i in c.description]
            print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
            DISH_ID=int(input("ENTER THE Id OF THE ITEM: "))
            QUERY="""DELETE FROM MENU WHERE DISH_NAME=(%s) and DISH_ID=(%s)"""
            VALUE=(DISH_NAME,DISH_ID,)
            c.execute(QUERY,VALUE)
            b.commit()
            print("✅ REMOVE SUCCESSFULLY")
            
    else:
        print("INVALID CHOICE!!| choose wisely|")


def UPDATE_MENU_ITEMS():
    print("😍 WANNA UPDATE SOMETHING IN MENU")
    print()
    print("HOW MANY ITEMS DO YOU WANT TO UPDATE?")
    a=int(input("ENTER THE NO. OF ITEMS FOR UPDATE: "))
    for i in range (1,a+1):
        print("❌DISH_ID CANNOT BE CHANGED")
        print("1.ITEM_NAME")
        print("2.ITEM_PRICE")
        print("3.STATUS")
        enter_choice=int(input("ENTER YOUR CHOICE: "))
        if enter_choice==1:
            p=input("ENTER DISH NAME YOU WANT TO UPDATE")
            Q="""SELECT*FROM MENU WHERE DISH_NAME=%s"""
            value=(p,)
            c.execute(Q,value)
            data=c.fetchall()
            headers=[i[0] for i in c.description]
            print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
            Id=int(input("ENTER DISH_Id: "))
            NAME=input("ENTER NEW NAME OF DISH: ")
            query="""UPDATE MENU 
                     SET DISH_NAME=%s
                     WHERE DISH_NAME=%s and DISH_Id=%s"""
            values=(p,NAME,Id)
            c.execute(query,values)
            b.commit()
            print("✅UPDATE SUCCESSFULLY")
        elif enter_choice==2:
            p=float(input("ENTER ITEM OLD PRICE: "))
            Q="""select*from MENU WHERE price=%s"""
            value=(p,)
            c.execute(Q,p)
            data=c.fetchall()
            headers=[i[0] for i in c.description]
            print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
            Id=int(input("ENTER THE DISH ID"))
            NEW_PRICE=float=input("ENTER THE NEW_PRICE ")
            query="""UPDATE MENU 
                     SET PRICE=%s
                     where DISH_Id=%s"""
            value=(NEW_PRICE,Id,)
            c.execute(query,value)
            b.commit()
            print("✅✅UPDATED SUCCESFULL")
        elif enter_choice==3:
            p=input("ENTER ITEM OLD status: ")
            Q="""select*from MENU WHERE status=%s"""
            value=(p,)
            c.execute(Q,p)
            data=c.fetchall()
            headers=[i[0] for i in c.description]
            print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
            Id=int(input("ENTER THE DISH ID"))
            NEW_STATUS=input("ENTER THE NEW_STATUS ")
            query="""UPDATE MENU 
                     SET STATUS=%s
                     where DISH_Id=%s"""
            value=(NEW_STATUS,Id,)
            c.execute(query,value)
            b.commit()
            print("✅✅UPDATED SUCCESFULL")
        else:
            print()
            print("INVALID ! CHOICE")

            
def ADD_ITEMS_IN_MENU():
    print("HOW MANY ITEMS YOU WANT TO ADD IN MENU?")
    a=int(input("ENTER A NUMBER OF ITEMS YOU WANT TO ADD: "))
    for i in range(1,a+1):
        print()
        DISH_NAME=input("ENTER A ITEM NAME: ")
        DISH_PRICE=float(input("ENTER A ITEM PRICE: "))
        QUERY="""INSERT INTO MENU(DISH_NAME,PRICE) 
                                           VALUES(%s,%s)"""
        value=(DISH_NAME,DISH_PRICE,)
        c.execute(QUERY,value)
        b.commit()
        print("✅ ITEM ADDED SUCCESSFULLY" )

#--------------------------------------------------------------------------------------------------
#➡️➡️FOR ORDER 
def view_order():
    q="select*from orders"
    c.execute(q)
    data=c.fetchall()
    headers=[i[0] for i in c.description]
    print(tabulate(data,headers=headers,tablefmt="fancy_grid"))



def order():
    view_menu()
    a=int(input("HOW MANY DISH YOU WANT TO ORDER?....  "))
    TABLE_NUMBER=int(input("ENTER YOUR TABLE_NUMBER: "))
    for i in range(0,a):
        Id=int(input("ENTER DISH ID: "))
        quantity=int(input("ENTER THE QUANTITY: "))
        query="""SELECT DISH_ID,DISH_NAME,STATUS,PRICE FROM MENU WHERE DISH_Id=(%s)"""
        value=(Id,)
        c.execute(query,value)
        data=c.fetchone()
        if data:
            DISH_ID, DISH_NAME, STATUS, PRICE = data
            total_price = PRICE * quantity
            
            # Insert order details into the orders table
            insert_query = """INSERT INTO ORDERS (DISH_ID, DISH_NAME, STATUS, PRICE,QUANTITY,TOTAL_PRICE,TABLE_NUMBER) 
                              VALUES (%s, %s, %s, %s, %s,%s,%s)"""
            insert_values = (DISH_ID, DISH_NAME, STATUS,PRICE, quantity, total_price,TABLE_NUMBER)
            c.execute(insert_query, insert_values)
            b.commit()
            print(f"Order placed for {quantity} x {DISH_NAME} at a total price of {total_price}.")
        else:
            print(f"No dish found with ID {Id}. Please check the menu and try again.")

def cancel_order():
    TABLE_NUMBER=int(input("ENTER YOUR TABLE NUMBER :  "))
    print("WANT TO CANCEL ORDER ?")
    print('1.CANCEL ALL ORDER')
    print("2.FOR CANCEL ONE ORDER ")
    ENTER_CHOICE=int(input('ENTER  YOUR CHOICE: '))
    if ENTER_CHOICE==1:
        q="DELETE FROM ORDERS WHERE TABLE_NUMBER=%s"
        value=(TABLE_NUMBER,)
        c.execute(q,value)
        b.commit()
        print("✅✅✅ALL ORDERS OF THIS TABLE CANCEL")
    elif ENTER_CHOICE==2:
        s="select*from orders where table_number=%s"
        value=(TABLE_NUMBER,)
        c.execute(s,value)
        data=c.fetchall()
        headers=[i[0] for i in c.description]
        print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
        Id=int(input("ENTER THE ID: "))
        Q="""DELETE FROM ORDERS WHERE TABLE_NUMBER=%s and DISH_ID=%s"""
        values=(TABLE_NUMBER,Id,)
        c.execute(Q,values)
        b.commit()
        print("✅✅DELETED SUCCESSFULLYYYYYYYYY")

def update_order_quantity():
    TABLE_NUMBER=int(input("ENTER YOUR TABLE NUMBER :  "))
    print("WANT TO UPDATE ORDER QUANTITY?")
    print('1.UPDATE ALL ORDER QUANTITY')
    print("2.FOR UPDATE ONE ORDER QUANTITY ")
    enter_choice=int(input("ENTER YOUR CHOICE: "))
    if enter_choice==1:
        s="select*from orders where table_number=%s"
        value=(TABLE_NUMBER,)
        c.execute(s,value)
        data=c.fetchall()
        headers=[i[0] for i in c.description]
        print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
        NEW_QUANTITY=int(input("ENTER THE NEW QUANTITY: "))
        query="""UPDATE ORDERS SET QUANTITY=%s WHERE TABLE_NUMBER=%s"""
        values=(NEW_QUANTITY,TABLE_NUMBER,)
        c.execute(query,values)
        b.commit()
        print("✅✅UPDATED SUCCESSFULLYYYYYYYYY")
    elif enter_choice==2:
        print("WANT TO UPDATE QUANTITY OF ONE ORDER")
        s="select*from orders where table_number=%s"
        value=(TABLE_NUMBER,)
        c.execute(s,value)
        data=c.fetchall
        headers=[i[0] for i in c.description]
        print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
        Id=int(input("ENTER THE ID: "))
        NEW_QUANTITY=int(input("ENTER THE NEW QUANTITY: "))
        query="""UPDATE ORDERS SET QUANTITY=%s WHERE TABLE_NUMBER=%s and DISH_ID=%s"""
        values=(NEW_QUANTITY,TABLE_NUMBER,Id,)
        c.execute(query,values)
        b.commit()
        print("✅✅UPDATED SUCCESSFULLYYYYYYYYY")
    else:
        print("INVALID CHOICE!!| choose wisely|")

#-------------------------------------------------------------------------------------------------------------#
#FOR CUSTOMER BOOKING MANAGEMENT 

def view_booking():
    q="select*from booking"
    c.execute(q)
    data=c.fetchall()
    headers=[i[0] for i in c.description]
    print(tabulate(data,headers=headers,tablefmt="fancy_grid"))


def add_booking():
    print("HOW MANY CUSTOMERS YOU WANT TO ADD IN BOOKING?")
    a=int(input("ENTER A NUMBER OF CUSTOMERS YOU WANT TO ADD: "))
    for i in range(1,a+1):
        print()
        NAME=input("ENTER A NAME: ")
        PHONE_NUMBER=input("ENTER A PHONE NUMBER: ")
        EMAIL=input("ENTER A EMAIL: ")
        CHECK_IN_DATE=input("ENTER CHECK IN DATE IN YYYY-MM-DD FORMAT KINDLY: ")
        CHECK_OUT_DATE=input("ENTER CHECK OUT DATE IN YYYY-MM-DD FORMAT KINDLY: ")
        ROOM_TYPE=input("ENTER ROOM TYPE: ")
        QUERY="""INSERT INTO BOOKING(BOOKING_ID,USER_NAME,BOOKING_DAYS,CUSTOMER_EMAIL,CHECK_IN_DATE,CHECK_OUT_DATE,ROOM_TYPE,ROOM_NUMBER,PRICEMNN) 
                                           VALUES(%s,%s,%s,%s,%s,%s)"""
        value=(NAME,PHONE_NUMBER,EMAIL,CHECK_IN_DATE,CHECK_OUT_DATE,ROOM_TYPE,)
        c.execute(QUERY,value)
        b.commit()
        print("✅ CUSTOMER ADDED SUCCESSFULLY" )





















#coding for admin
print("**********WELCOME TO THE HOTEL SYSTEM***********")
print("1.ADMIN")
print("2.customer")
print("3.staff")
print("4.exit")
choice=int(input("ENTER YOUR CHOICE: "))

if choice==1:
    while True:
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
                    print("WELCOME BACK ADMIN")
                    print()
                    print()
                    print("************WELCOME TO ADMIN SECTION************")
                    print("1.STAFF MANAGEMENT")
                    print("2.RESTURANT MANAGEMENT")
                    print("3.CUSTOMER BOOKING MANAGEMENT")
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
                            print("4.UPDATE IN STAFF")
                            print("5.exit")
                            enter_choice=int(input("ENTER YOUR CHOICE: "))
                    
                            if enter_choice==1:
                                 view_staff()
                                
                            elif enter_choice==2:
                                 HIRE_STAFF()
                                    
                            elif enter_choice==3:
                                REMOVE_STAFF()
                                
                                
                            elif enter_choice==4:
                                UPDATE_IN_STAFF()
                            elif enter_choice==5:
                                break
                            else:
                                print("INVALID OUTPUT")      
                    elif admin_choice2==2:
                        while True:
                            print("*****WELCOME TO RESTURANT MANAGEMENT*****")
                            print("1.VIEW MENU")
                            print("2.ADD ITEM IN MENU")
                            print("3.DELETE ITEM IN MENU ")
                            print("4.UPDATE MENU")
                            print("5.ORDERS")
                            print("6.EXIT")
                            enter_choice=int(input("ENTER YOUR CHOICE: "))
                            if enter_choice==1:
                                c.execute("select*from menu")
                                data=c.fetchall()
                                headers=[i[0] for i in c.description]
                                print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
                                
                            elif enter_choice==2:
                                ADD_ITEMS_IN_MENU()
                                # Function to add menu items  
                                pass
                            elif enter_choice==3:
                                DELETE_ITEMS_IN_MENU()
                                #FUNCTION TO DELETE ITEMS FROM MENU
                            elif enter_choice==4:
                                UPDATE_MENU_ITEMS()
                                #FUNCTION TO UPDATE_MENU_ITEMS
                            elif enter_choice==5:
                                while True:
                                    print()
                                    print("**WELCOME TO ORDER SECTION**")
                                    print("1.VIEW ORDER ")
                                    print("2.DO ORDER ")
                                    print("3.CANCEL ORDER ")
                                    print("4.UPDATE ORDER ")
                                    print("5.exit")     
                                    order_choice=int(input("ENTER YOUR CHOICE: "))
                                    if order_choice==1:
                                        view_order()
                                        print("THE TOTAL ORDER!")
                                    elif order_choice==2:
                                        order()
                                        print()
                                    elif order_choice==3:
                                        cancel_order()
                                    elif order_choice==4:
                                        update_order_quantity()
                                    elif order_choice==5:
                                        break
                                    else:   
                                        print("INVALID CHOICE")
                            elif enter_choice==6:
                                break
                    elif admin_choice2==3:
                        print("CUSTOMER BOOKING  MANAGEMENT SECTION")
                        print("1.VIEW ALL CUSTOMER BOOKING")
                        print("2.DO CUSTOMEER BOOKING ")
                        print("3.CANCEL CUSTOMER BOOKING ")
                        print("4.UPDATE CUSTOMER")
                        print("5.exit")
                        customer_choice=int(input("ENTER YOUR CHOICE: "))
                        if customer_choice==1:
                            view_booking()
                            # Function to view customers
                            pass
                        elif customer_choice==2:
                            # Function to add customers
                            pass
                        elif customer_choice==3:
                            # Function to delete customers
                            pass
                        elif customer_choice==4:
                            # Function to update customers
                            pass
                        elif customer_choice==5:
                            break                      