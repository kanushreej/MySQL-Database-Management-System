import mysql.connector

def connector():
    mysql.connector.connect(
    host="localhost",
    user="root",
    password="x",
    database="library")

mydb = connector()

def view():
    from prettytable import PrettyTable
    mydb = connector()
    c = mydb.cursor()
    print()
    c.execute("select * from books")
    print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
    print()
                
    table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
    myresult=c.fetchall()
    for i in myresult:
        table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

    print(table)
    print()    
    mydb.commit()
    
    
def filter():
    print()
    print(" - - - - - - - - - - BOOK FILTER - - - - - - - - - - ")
    print()
    print("SELECT YOUR DESIRED FILTER")
    print("1. BOOK")
    print("2. AUTHOR")
    print("3. PRICE")
    print("4. CATEGORY")
    print("5. CODE")
    print("6. STATUS")
    print("7. EXIT")
    print()
    ch1=int(input("ENTER YOUR CHOICE: "))

    while True: 
        if ch1==1:
            print()
            book=input("ENTER BOOK: ")
            from prettytable import PrettyTable
            x=mydb.cursor()

            x.execute("select * from books where book='{}'".format(book))
            rec=x.fetchall()

            if len(rec)!=0:
                print()
                print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
                table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
                for i in rec:
                 table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

                print(table)
                print()    
                mydb.commit()
        

            elif len(rec)==0:
                    print()
                    print("BOOK NOT FOUND")
                    print()
                    print('*'*100)

        elif ch1==2:
            print()
            author=input("ENTER AUTHOR: ")
            from prettytable import PrettyTable
            x=mydb.cursor()

            x.execute("select * from books where author='{}'".format(author))
            rec=x.fetchall()

            if len(rec)!=0:
                print()
                print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
                table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
                for i in rec:
                 table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

                print(table)
                print()    
                mydb.commit()
        

            elif len(rec)==0:
                    print()
                    print("BOOK NOT FOUND")
                    print()
                    print('*'*100)


        elif ch1==3:
            print()
            print("SELECT PRICE SPECIFICATIONS")
            print("1. SPECIFIC PRICE")
            print("2. PRICE RANGE")
            ch13=int(input("ENTER YOUR CHOICE: "))

            if ch13==1:
             print()
             price=int(input("ENTER PRICE: "))
             from prettytable import PrettyTable
             x=mydb.cursor()

             x.execute("select * from books where price='{}'".format(price))
             rec=x.fetchall()

             if len(rec)!=0:
                print()
                print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
                table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
                for i in rec:
                 table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

                print(table)
                print()    
                mydb.commit()
        

             elif len(rec)==0:
                    print()
                    print("BOOK NOT FOUND")
                    print()
                    print('*'*100)
                    break

            elif ch13==2:
                print()
                p1=int(input("ENTER LOWER RANGE: "))
                p2=int(input("ENTER UPPER RANGE: "))
                from prettytable import PrettyTable
                x=mydb.cursor()

                x.execute("select * from books where price between '{}' and '{}'".format(p1,p2))
                rec=x.fetchall()

                if len(rec)!=0:
                 print()
                 print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
                 table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
                 for i in rec:
                  table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

                 print(table)
                 print()    
                 mydb.commit()
        

                elif len(rec)==0:
                    print()
                    print("BOOK NOT FOUND")
                    print()
                    print('*'*100)
                

        elif ch1==4:

            print("SELECT CATEGORY")
            print("1. FICTION")
            print("2. NON-FICTION")
            ch14=int(input("ENTER YOUR CHOICE: "))

            if ch14==1:
             from prettytable import PrettyTable
             x=mydb.cursor()

             x.execute("select * from books where category='Fiction'")
             rec=x.fetchall()

             if len(rec)!=0:
                print()
                print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
                table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
                for i in rec:
                 table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

                print(table)
                print()    
                mydb.commit()
        

             elif len(rec)==0:
                    print()
                    print("BOOK NOT FOUND")
                    print()
                    print('*'*100)

            elif ch14==2:
                from prettytable import PrettyTable
                x=mydb.cursor()

                x.execute("select * from books where category='Non-Fiction'")
                rec=x.fetchall()

                if len(rec)!=0:
                 print()
                 print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
                 table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
                 for i in rec:
                  table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

                 print(table)
                 print()    
                 mydb.commit()
        

                elif len(rec)==0:
                    print()
                    print("BOOK NOT FOUND")
                    print()
                    print('*'*100)

        elif ch1==5:
            print()
            code=int(input("ENTER CODE: "))
            from prettytable import PrettyTable
            x=mydb.cursor()

            x.execute("select * from books where code='{}'".format(code))
            rec=x.fetchall()

            if len(rec)!=0:
                print()
                print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
                table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
                for i in rec:
                 table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

                print(table)
                print()    
                mydb.commit()
        

            elif len(rec)==0:
                    print()
                    print("BOOK NOT FOUND")
                    print()
                    print('*'*100)

        elif ch1==6:
            
            print("SELECT CATEGORY")
            print("1. AVAILABLE")
            print("2. UNAVAILABLE")
            ch14=int(input("ENTER YOUR CHOICE: "))

            if ch14==1:
             from prettytable import PrettyTable
             x=mydb.cursor()

             x.execute("select * from books where status='Available'")
             rec=x.fetchall()

             if len(rec)!=0:
                print()
                print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
                table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
                for i in rec:
                 table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

                print(table)
                print()    
                mydb.commit()
        

             elif len(rec)==0:
                    print()
                    print("BOOK NOT FOUND")
                    print()
                    print('*'*100)

            elif ch14==2:
                from prettytable import PrettyTable
                x=mydb.cursor()

                x.execute("select * from books where status='Unavailable'")
                rec=x.fetchall()

                if len(rec)!=0:
                 print()
                 print(" - - - - - - - - - - LIBRARY BOOKS - - - - - - - - - - ")
                 table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
                 for i in rec:
                  table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

                 print(table)
                 print()    
                 mydb.commit()
        

                elif len(rec)==0:
                    print()
                    print("BOOK NOT FOUND")
                    print()
                    print('*'*100)

            elif ch1==7:
                break

            else:
                print("INCORRECT OPTION, TRY AGAIN!")


def ex_user():
    un=input("ENTER USERNAME: ")
    pw=input("ENTER PASSWORD: ")
    
    from prettytable import PrettyTable
    mydb = connector()
    c = mydb.cursor()
    print()
    c.execute("select * from user where username='{}' and password='{}'".format(un,pw))

    print(" - - - - - - - - - - USER DETAILS - - - - - - - - - - ")
    print()
                
    table=PrettyTable(["FIRST NAME","LAST NAME","PHONE","EMAIL"])
    myresult=c.fetchall()
    for i in myresult:
        table.add_row([i[0],i[1],i[2],i[3]])

    print(table)


    print()    
    mydb.commit()

    print(" - - - - - - - - - - BOOK PURCHASING - - - - - - - - - - ")
    view()

    b1=input("ENTER NAME OF FIRST BOOK: ")
    b2=input("ENTER NAME OF SECOND BOOK: ")
    b3=input("ENTER NAME OF THIRD BOOK: ")

    c.execute("update user set book1='{}',book2='{}',book3='{}' where username='{}' and password='{}'".format(b1,b2,b3,un,pw))

    print(" - - - - - - - - - - YOUR BOOKS - - - - - - - - - - ")

    c.execute("select * from books where book='{}'or book='{}'or book='{}'".format(b1,b2,b3))
    print()       
    table=PrettyTable(["BOOK","AUTHOR","PRICE","CATEGORY","CODE","STATUS"])
    myresult=c.fetchall()
    for i in myresult:
        table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

    print(table)


    print()    
    mydb.commit()

    c.execute("select sum(price) from books where book='{}'or book='{}'or book='{}'".format(b1,b2,b3))
    myresult=c.fetchall()

    pp=myresult[0][0]

    c.execute("update user set price='{}' where username='{}' and password='{}'".format(pp,un,pw))

    print(" - - - - - - - - - - CHECKOUT - - - - - - - - - - ")

    c.execute("select book1,book2,book3,price from user where username='{}' and password='{}'".format(un,pw))
    print()
    table=PrettyTable(["BOOK1","BOOK2","BOOK3","PRICE"])
    myresult=c.fetchall()
    for i in myresult:
        table.add_row([i[0],i[1],i[2],i[3]])

    print(table)
    print()
    print("CONGRATULATIONS! YOU HAVE BOUGHT THREE BOOKS!")

def new_user():
    print()
    print(" - - - - - - - - - - NEW USER ACCOUNT SET-UP - - - - - - - - - - ")
    print()
    fn=input("ENTER FIRST NAME: ")
    ln=input("ENTER LAST NAME: ")
    phone=int(input("ENTER PHONE NUMBER: "))
    email=input("ENTER EMAIL: ")
    username=input("ENTER USERNAME: ")
    password=input("ENTER PASSWORD: ")

    mydb = connector()
    c = mydb.cursor()

    c.execute("insert into user(first_name,last_name,phone,email,username,password) values ('{}','{}','{}','{}','{}','{}')".format(fn,ln,phone,email,username,password))
    print("CONGRATULATIONS! YOUR ACCOUNT HAS BEEN MADE!")

    mydb.commit()

def user_data():
    
    from prettytable import PrettyTable
    mydb = connector()
    c = mydb.cursor()
    print()
    c.execute("select * from user")

    print(" - - - - - - - - - - USER DETAILS - - - - - - - - - - ")
    print()
                
    table=PrettyTable(["FIRST NAME","LAST NAME","PHONE","EMAIL","USERNAME","PASSWORD","BOOK1","BOOK2","BOOK3","PRICE"])
    myresult=c.fetchall()
    for i in myresult:
        table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])

    print(table)


    print()    
    mydb.commit()

def employee_data():
    from prettytable import PrettyTable
    mydb = connector()
    c = mydb.cursor()
    print()
    c.execute("select * from employee")

    print(" - - - - - - - - - - EMPLOYEE DETAILS - - - - - - - - - - ")
    print()
                
    table=PrettyTable(["FIRST NAME","LAST NAME","PHONE","EMAIL","USERNAME","PASSWORD","DESIGNATION","SALARY"])
    myresult=c.fetchall()
    for i in myresult:
        table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])

    print(table)


    print()    
    mydb.commit()

def emp_login():
    un=input("ENTER USERNAME: ")
    pw=input("ENTER PASSWORD: ")
    
    from prettytable import PrettyTable
    mydb = connector()
    c = mydb.cursor()
    print()
    
    c.execute("select * from employee where username='{}' and password='{}'".format(un,pw))
    rec=c.fetchall()
    
    if rec!=0:
            
        print(" - - - - - - - - - - EMPLOYEE DETAILS - - - - - - - - - - ")
        print()
                    
        table=PrettyTable(["FIRST NAME","LAST NAME","PHONE","EMAIL","USERNAME","PASSWORD","DESIGNATION","SALARY"])
        for i in rec:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])

        print(table)


        print()    
        mydb.commit()

    else:
        print("EMPLOYEE NOT FOUND")
    



def modify():
    
    print("SELECT HOW YOU WOULD LIKE TO MODIFY THE LIBRARY")
    print("1. ADD NEW RECORDS")
    print("2. DELETE OLD RECORDS")
    print("3. UPDATE OLD RECORDS")
    print("4. DISPLAY ALL RECORDS")
    print("5. EXIT")
    print()
    op=int(input("SELECT YOUR CHOICE: "))

    if op==1:

        print(" - - - - - - - - - - ADDING NEW RECORDS - - - - - - - - - - ")
        print()
        
        mydb = connector()
        c = mydb.cursor()
        
        book=input("ENTER BOOK: ")
        author=input("ENTER AUTHOR: ")
        price=int(input("ENTER PRICE: "))
        cat=input("ENTER CATEGORY: ")
        code=int(input("ENTER CODE: "))
        stat=input("ENTER STATUS: ")

        c.execute("insert into books(book,author,price,category,code,status) values ('{}','{}','{}','{}','{}','{}')".format(book,author,price,cat,code,stat))
             
        print("NEW RECORD HAS BEEN ADDED!")    
        mydb.commit()

    elif op==2:
        print(" - - - - - - - - - - DELETING OLD RECORDS - - - - - - - - - - ")
        print()
        
        mydb = connector()
        c = mydb.cursor()
        
        book=input("ENTER BOOK TO DELETE: ")

        c.execute("delete from books where book='{}'".format(book))
             
        print("RECORD HAS BEEN DELETED!")    
        mydb.commit()

    elif op==3:
        
        print(" - - - - - - - - - - UPDATING OLD RECORDS - - - - - - - - - - ")
        print()
        print("SELECT WHAT TO UPDATE")
        print("1. BOOK")
        print("2. AUTHOR")
        print("3. PRICE")
        print("4. CATEGORY")
        print("5. CODE")
        print("6. STATUS")
        print()
        ch=int(input("SELECT YOUR CHOICE: "))

        if ch==1:
            print(" - - - - - - - - - - UPDATING BOOK NAME - - - - - - - - - - ")
            print()

            book=input("ENTER NAME OF BOOK TO UPDATE: ")
            b=input("ENTER NEW NAME OF BOOK: ")
            
            mydb = connector()
            c = mydb.cursor()

            c.execute("update books set book='{}' where book='{}'".format(b,book))

            print()
            print("RECORD HAS BEEN UPDATED!")

            mydb.commit()

        if ch==2:
            print(" - - - - - - - - - - UPDATING AUTHOR NAME - - - - - - - - - - ")
            print()

            book=input("ENTER NAME OF BOOK TO UPDATE: ")
            a=input("ENTER NEW NAME OF AUTHOR: ")
            
            mydb = connector()
            c = mydb.cursor()

            c.execute("update books set author='{}' where book='{}'".format(a,book))

            print()
            print("RECORD HAS BEEN UPDATED!")

            mydb.commit()

        if ch==3:
            print(" - - - - - - - - - - UPDATING BOOK PRICE - - - - - - - - - - ")
            print()

            book=input("ENTER NAME OF BOOK TO UPDATE: ")
            p=int(input("ENTER NEW PRICE OF BOOK: "))
            
            mydb =connector()
            c = mydb.cursor()

            c.execute("update books set price='{}' where book='{}'".format(p,book))

            print()
            print("RECORD HAS BEEN UPDATED!")

            mydb.commit()

        if ch==4:
            print(" - - - - - - - - - - UPDATING BOOK CATEGORY - - - - - - - - - - ")
            print()

            book=input("ENTER NAME OF BOOK TO UPDATE: ")
            cc=input("ENTER NEW CATEGORY OF BOOK: ")
            
            mydb = connector()
            c = mydb.cursor()

            c.execute("update books set category='{}' where book='{}'".format(cc,book))

            print()
            print("RECORD HAS BEEN UPDATED!")

            mydb.commit()

        if ch==5:
            print(" - - - - - - - - - - UPDATING BOOK CODE - - - - - - - - - - ")
            print()

            book=input("ENTER NAME OF BOOK TO UPDATE: ")
            ccc=int(input("ENTER NEW CODE OF BOOK: "))
            
            mydb = connector()
            c = mydb.cursor()

            c.execute("update books set code='{}' where book='{}'".format(ccc,book))

            print()
            print("RECORD HAS BEEN UPDATED!")

            mydb.commit()

        if ch==6:
            print(" - - - - - - - - - - UPDATING BOOK STATUS - - - - - - - - - - ")
            print()

            book=input("ENTER NAME OF BOOK TO UPDATE: ")
            s=input("ENTER NEW STATUS OF BOOK: ")
            
            mydb = connector()
            c = mydb.cursor()

            c.execute("update books set status='{}' where book='{}'".format(s,book))

            print()
            print("RECORD HAS BEEN UPDATED!")

            mydb.commit()

    elif op==4:
        view()

while True:
    
    print()
    print("                      - - - - - - - - - - - - - ! WELCOME TO THE ONLINE REGENSTEIN LIBRARY ! - - - - - - - - - - - - - " )

    print()
    print()

    print("SELECT YOUR DESIRED OPTION")
    print("1. VIEW BOOKS ")
    print("2. BUY BOOKS ")
    print("3. EMPLOYEE LOGIN ")
    print("4. EXIT ")

    print()

    ch=int(input("ENTER YOU CHOICE: "))

    if ch==1:

        print(" - - - - - - - - - - VIEWING BOOKS - - - - - - - - - - ")
        print()
        print("SELECT METHOD OF VIEWING")
        print("1. VIEW ALL BOOKS")
        print("2. ADD FILTER TO VIEW SPECIFIC BOOKS")
        print("3. EXIT")
        print()
        option1=int(input("SELECT CHOICE: "))
        
        if option1==1:
            view()
            
        elif option1==2:
            filter()

        elif option1==3:
            break

        else:
            print("INCORRECT OPTION, TRY AGAIN")
            

    elif ch==2:
        print()
        print(" - - - - - - - - - - BUYING BOOKS - - - - - - - - - - ")
        print()
        print("TO BUY BOOKS YOU MUST HAVE AN ACCOUNT")
        print("SELECT OPTION")
        print("1. EXISTING USER")
        print("2. NEW USER")
        print("3. EXIT")
        print()
        option2=int(input("SELECT CHOICE: "))
        
        if option2==1:
            ex_user()
            
        elif option2==2:
            new_user()

        elif option2==3:
            break

        else:
            print("INCORRECT OPTION, TRY AGAIN")

    elif ch==3:
        print()
        print(" - - - - - - - - - - EMPLOYEE LOGIN - - - - - - - - - - ")

        emp_login()
        print("SELECT OPTION")
        print("1. VIEW USER DATA")
        print("2. VIEW EMPLOYEE DATA")
        print("3. MODIFY LIBRARY")
        print("4. EXIT")
        print()
        option3=int(input("SELECT CHOICE: "))

        if option3==1:
            print()
            user_data()

        elif option3==2:
            print()
            employee_data()

        elif option3==3:
            print()
            modify()

        elif option3==4:
            break

        else:
            print("INCORRECT OPTION, TRY AGAIN")

    elif ch==4:
        break

    else:
        print("INCORRECT OPTION, TRY AGAIN")

            
            

                    

        


        
        
        
        

    
    



        
    
    



























































    
                 
                 
