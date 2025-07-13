from tabulate import tabulate
import pymysql as  a 
b=a.connect (host="localhost",  user="root",  password="Azra@9758547293",  database="hotelmanagementproject")
print(F"CONNECTED SUCCESSFULLY TO THE DATABASE")
c=b.cursor()
print()


#✨✨✨✨✨✨✨✨✨✨✨✨✨✨function required to make for ADMIN✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨ 
#------------------------------------------------------------------------------------------------------------------
#➡️FOR STAFF MANAGEMENT

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
        
          
#------------------------------------------------------------------------------------------------------#--          
#➡️➡️FUNCTION FOR RESTURANT 

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
                    print("cool👌")
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
                            print("4.UPDATE IN STAFF")
                            print("5.exit")
                            enter_choice=int(input("ENTER YOUR CHOICE: "))
                    
                            if enter_choice==1:
                                c.execute("select*from employes")
                                data=c.fetchall()
                                headers=[i[0] for i in c.description]
                                print(tabulate(data,headers=headers,tablefmt="fancy_grid"))
                                
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
                            print("5.DO ORDER ")
                            print("6.CANCEL ORDER")
                            print("7.UPDATE ORDER")
                            print("8.exit")
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
