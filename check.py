import math
import os
def DispMenu():
    print("\n\n\n\t\t############ LIBRARY MANAGEMENT ###############")
    print("\n\t\t\t 1. BOOK MANAGEMENT ")
    print("\n\t\t\t 2. MEMBER MANAGEMENT ")
    print("\n\t\t\t 3. ISSUE BOOK")
    print("\n\t\t\t 4. RETURN BOOK")
    print("\n\t\t\t 5. EXIT ")
    print("\t\t######################################################")
    def BookMenu():
        print("\n\n\n\t\t############ BOOK MANAGEMENT ###############")
        print("\n\t\t\t 1. ADD BOOK  ")
        print("\n\t\t\t 2. DELETE BOOK ")
        print("\n\t\t\t 3. MODIFY BOOK")
        print("\n\t\t\t 4. DISPLAY BOOKS")

print("\n\t\t\t 5. EXIT ")
print("\t\t##################################################")
def MemberMenu():
    print("\n\n\n\t\t############ MEMBER MANAGEMENT ###############")
    print("\n\t\t\t 1. ADD MEMBER  ")
    print("\n\t\t\t 2. DELETE MEMBER ")
    print("\n\t\t\t 3. MODIFY MEMBER")
    print("\n\t\t\t 4. DISPLAY MEMBERS")
    print("\n\t\t\t 5. EXIT ")
    print("\t\t##################################################")
def bookadd():
        import mysql.connector        # Import MySQL 
        con1 = mysql.connector.connect(host='localhost', database='world', user='root', password='tiger')                     # Open a connection to a database
        cursor1 = con1.cursor()           #Create a cursor object#Execute SQL query to insert records in the table newitems        
        print("Enter the following information")


        bno=input("Enter the book number:")
        bname=input("Enter book name:")
        bauthor=input("Enter author name:")
        bprice=float(input("Enter book price:"))
        bstat="N"
        sql_query=("insert into book (bookno, bookname, bookauthor, bookprice, status) values (%s,%s,%s,%s,%s);")
        insert_data=(bno,bname,bauthor,bprice,bstat)
        cursor1.execute(sql_query,insert_data)
        con1.commit()     # Stores the data permanently in the table
        con1.close()      #Close connection object
        cursor1.close()   #Close cursor object
        print("book added")

def bookdelete():
    bno=input("Enter book Number to be deleted")
    flag=0
    import mysql.connector          # Import MySQL 
    con1 = mysql.connector.connect(host='localhost', database='world', user='root', password='tiger')                      # Open a connection to a database
    
    cursor1 = con1.cursor()           #Create a cursor object#Execute SQL query to update the table
    cursor1.execute("delete from book where bookno = %s",(bno,))
    con1.commit()                           # Stores the data permanently in the table
    con1.close()                                #Close connection object
    cursor1.close()
def bookmodify():
    import mysql.connector        # Import MySQL connector
    con1 = mysql.connector.connect(host='localhost', database='world', user='root', password='tiger')                     # Open a connection to a database
    cursor1 = con1.cursor()           #Create a cursor object#Execute SQL query to insert records in the table 
    bno=input("Enter the book number you want to modify")    
    print("Enter the following information")
    bname=input("Enter book name:")
    bauthor=input("Enter author name:")
    bprice=input("Enter book price:")

    bstat="N"
    cursor1.execute("update book set bookname=%s, bookauthor=%s, bookprice=%s, status=%s where bookno=%s",(bname,bauthor,bprice,bstat,bno))
    con1.commit()     # Stores the data permanently in the table
    con1.close()                                #Close connection object
    cursor1.close()#Close cursor object
    print("book modified")
def bookdisp():
    import mysql.connector        # Import MySQL connector
    con1 = mysql.connector.connect(host='localhost', database='world', user='root', password='tiger')                     # Open a connection to a database
    cursor1 = con1.cursor()           #Create a cursor object
    cursor1.execute ("select * from book;")  #Execute SQL query to create a table# fetch all rows of a result set and store in rs as a list of tuples
    rs = cursor1.fetchall()
    print("\n\n\n########################## BOOK DETAILS #############################")
    print("%10s"%"BOOKNO.","%20s"%"TITLE","%20s"%"AUTHOR","%15s"%"PRICE", "%15s"%"STATUS")

    for row in rs:
        # for loop to display all records
        print("%10s"%row[0],"%20s"%row[1],"%20s"%row[2],"%15s"%row[3],"%15s"%row[4])
        print("\n########################## BOOK DETAILS #############################")
        K=input("\n\nPress any key to continue")
        con1.close()                    #Close connection object
        cursor1.close()#Close cursor object
def memberadd():
    import mysql.connector        # Import MySQL connector
    con1 = mysql.connector.connect(host='localhost', database='world', user='root', password='tiger')                     # Open a connection to a databasec
    cursor1 = con1.cursor()
    #Create a cursorobject#Execute SQL query to insert records in the table newitems        
    print("Enter the following information")
    mno=input("Enter the member number:")
    mname=input("Enter member name:")
    mbno=" "
    bstat="N"
    sql_query=("insert into member1 (memberno, membername, booknum, memstatus) values (%s,%s,%s,%s);")
    insert_data=(mno,mname,mbno,bstat)
    cursor1.execute(sql_query,insert_data)
    con1.commit()     # Stores the data permanently in the table
    con1.close()      #Close connection object
    cursor1.close()   #Close cursor object
    print("Member added")
def memberdelete():
    mno=input("Enter member number to be deleted")
    flag=0
    import mysql.connector    # Import MySQL connector
    con1 = mysql.connector.connect(host='localhost', database='world', user='root', password='tiger')                      # Open a connection to a database

    cursor1 = con1.cursor()           #Create a cursor object#Execute SQL query to update the table
    cursor1.execute("delete from member1 where memberno = %s",(mno,))
    con1.commit()                           # Stores the data permanently in the table
    con1.close()                                #Close connection object
    cursor1.close()
    print("book deleted")

def membermodify():
    import mysql.connector        # Import MySQL connector
    con1 = mysql.connector.connect(host='localhost', database='world', user='root', password='tiger')                     # Open a connection to a database
    cursor1 = con1.cursor()           #Create a cursor object#Execute SQL query to insert records in the table newitems
    mno=input("Enter the member number you want to modify")    
    print("Enter the following information")    
    mname=input("Enter member name:")
    mbno=" "  
    mstat="N"

cursor1.execute("update member1 set membername=%s, booknum=%s, memstatus=%s where memberno=%s",(mname,mbno,mstat,mno))
con1.commit()     # Stores the data permanently in the table
con1.close()                                #Close connection object
cursor1.close()#Close cursor object
print("book modified")
def memberdisp():
    import mysql.connector        # Import MySQL connector
    con1 = mysql.connector.connect(host='localhost', database='world', user='root', password='tiger')                     # Open a connection to a database
    cursor1 = con1.cursor()           #Create a cursor object
    cursor1.execute ("select * from member1;")  #Execute SQL query to create a table# fetch all rows of a result set and store in rs as a list of tuples
    rs = cursor1.fetchall()
    print("\n\n\n########################## BOOK DETAILS #############################")
    print("%10s"%"MEMBER NO.","%20s"%"NAME","%20s"%"BOOK NUMBER","%15s"%"STATUS")
    for row in rs:                            # for loop to display all records
        print("%10s"%row[0],"%20s"%row[1],"%20s"%row[2],"%15s"%row[3])
        
        print("\n########################## BOOK DETAILS #############################")
        K=input("\n\nPress any key to continue")
        con1.close()                    #Close connection object
        cursor1.close()#Close cursor object
