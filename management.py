import mysql.connector as msc
from prettytable import PrettyTable

mydb = msc.connect(host="localhost",
                   user="root",
                   password="root",
                   allow_local_infile=True)
crs = mydb.cursor()

qry01 = "CREATE DATABASE if not exists blog"
crs.execute(qry01)
qry02 = "USE blog "
crs.execute(qry02)
qry03 = "CREATE TABLE if not exists Profile (id_profile int(10) primary key,Username varchar(25),Email varchar(25),Followers int(4),Following int(4),Owned_Posts int(20),Comments int(5));"
crs.execute(qry03)
qry31 = "INSERT INTO Profile   VALUES(0001,'AleXa','alx21@gmail.com',10,2,5,10)"
qry32 = "INSERT INTO  Profile   VALUES(0002,'Ram','ram00@gmail.com',4,2,1,2)"
qry33 = "INSERT INTO Profile   VALUES (0003,'Rony','rony@gmail.com',3,3,1,2)  "
qry34 = "INSERT INTO Profile    VALUES (0004,'Anna','anna@gmail.com',7,5,2,4)"
qry35 = "INSERT INTO Profile  VALUES(0005,'Lovera','ralov@gmail.com',0,4,0,0)  "
qry36 = "INSERT INTO Profile  VALUES (0006,'Andrea','32and@gmail.com',3,8,1,2)"
qry37 = "INSERT INTO Profile    VALUES(0007,'Mark','marklop@gmail.com',5,2,3,6)"
qry38 = "INSERT INTO Profile    VALUES(0008,'Sandra','zandra@gmail.com',0,3,4,8)"
qry39 = "INSERT INTO Profile    VALUES(0009,'Carlos','losandrew@gmail.com',1,1,2,5)"
qry40 = "INSERT INTO Profile    VALUES(0010,'Mike','mikelonch@gmail.com',5,4,1,3)  "
crs.execute(qry31)
crs.execute(qry32)
crs.execute(qry33)
crs.execute(qry34)
crs.execute(qry35)
crs.execute(qry36)
crs.execute(qry37)
crs.execute(qry38)
crs.execute(qry39)
crs.execute(qry40)

qry04 = "CREATE TABLE IF NOT EXISTS qns(id_profile int(10) ,Categories varchar(15) check(categories='MATHS' or categories='PHYSICS' or categories='CHEMISTRY' or categories='HISTORY' or categories='COMPUTER' ),question varchar(300));"
crs.execute(qry04)
qry51 = "INSERT INTO qns_ans VALUES (01,'MATHS','FACTORS OF 196')"
qry52 = "INSERT INTO qns_ans VALUES (01,'PHYSICS','WORKING PRINCIPLE OF A WASHING MACHINE')"
qry53 = "INSERT INTO qns_ans VALUES (01,'COMPUTER','WHO IS THE FATHER OF COMPUTER')"
qry54 = "INSERT INTO qns_ans VALUES (01,'CHEMISTRY','SOLUBILITY OF ALCOHOL IN WATER IS DUE TO')"
qry55 = "INSERT INTO qns_ans VALUES (01,'HISTORY','WHO WAS THE FIRST EMPEROR OF INDIA')"
qry56 = "INSERT INTO qns_ans VALUES (02,'MATHS','20+(90/2) IS EQUAL TO')"
qry57 = "INSERT INTO qns_ans VALUES (03,'HISTORY','WHO IS KNOWN AS THE FATHER OF INDIA')"
qry58 = "INSERT INTO qns_ans VALUES (04,'COMPUTER','WHAT IS THE FULLFORM OF CPU')"
qry59 = "INSERT INTO qns_ans VALUES (04,'PHYSICS','AN AIR BUBBLE IN WATER WILL ACT LIKE A')"
qry60 = "INSERT INTO qns_ans VALUES (06,'CHEMISTRY','WHO IS KNOWN AS FATHER OF CHEMISTRY')"
qry61 = "INSERT INTO qns_ans VALUES (07,'MATHS','WHAT IS THE NEXT 2 PRIME NUMBERS AFTER 5')"
qry62 = "INSERT INTO qns_ans VALUES (07,'MATHS','HOW MANY METERS ARE IN A KILOMETER')"
qry63 = "INSERT INTO qns_ans VALUES (07,'COMPUTER','THE ABBREVIATION BPS STANDS FOR')"
qry64 = "INSERT INTO qns_ans VALUES (08,'PHYSICS','WHO IS THE FATHER OF PHYSICS')"
qry65 = "INSERT INTO qns_ans VALUES (08,'HISTORY','WHO WAS THE FIRST WOMEN PRIME MINISTER OF INDIA')"
qry66 = "INSERT INTO qns_ans VALUES (08,'COMPUTER','SMALLEST UNIT OF DATA IN A COMPUTER')"
qry67 = "INSERT INTO qns_ans VALUES (08,'CHEMISTRY','THE STRONGEST METAL ON EARTH' )"
qry68 = "INSERT INTO qns_ans VALUES (09,'MATHS','HOW MANY FACES DOES A CUBE HAVE')"
qry69 = "INSERT INTO qns_ans VALUES (09,'PHYSICS','UNIT OF POWER')"
qry70 = "INSERT INTO qns_ans VALUES (010,'HISTORY','WHO WROTE THE INDIAN NATIONAL ANTHEM')"
crs.execute(qry51)
crs.execute(qry52)
crs.execute(qry53)
crs.execute(qry54)
crs.execute(qry55)
crs.execute(qry56)
crs.execute(qry57)
crs.execute(qry58)
crs.execute(qry59)
crs.execute(qry60)
crs.execute(qry61)
crs.execute(qry62)
crs.execute(qry63)
crs.execute(qry64)
crs.execute(qry65)
crs.execute(qry66)
crs.execute(qry67)
crs.execute(qry68)
crs.execute(qry69)
crs.execute(qry70)

qry05 = "CREATE TABLE IF NOT EXISTS comments(question varchar(50), comment varchar(20),foreign key(question) references qns_ans(question));"
crs.execute(qry05)
qry91 = "INSERT INTO comments VALUES('FACTORS OF 196','1,2,4,14,98')"
qry92 = "INSERT INTO comments VALUES('FACTORS OF 196','1,2,4,7,14,28,49,98,196')"
qry93 = "INSERT INTO comments VALUES('WORKING PRINCIPLE OF A WASHING MACHINE','CENTRIFUGATION')"
qry94 = "INSERT INTO comments VALUES('WORKING PRINCIPLE OF A WASHING MACHINE','DIFFUSION')"
qry95 = "INSERT INTO comments VALUES('WHO IS THE FATHER OF COMPUTER','CHARLES')"
qry96 = "INSERT INTO comments VALUES('WHO IS THE FATHER OF COMPUTER','CHARLES BABBAGE')"
qry97 = "INSERT INTO comments VALUES('SOLUBILITY OF ALCOHOL IN WATER IS DUE TO','HYDROGEN BONDING')"
qry98 = "INSERT INTO comments VALUES('SOLUBILITY OF ALCOHOL IN WATER IS DUE TO','OXIDATION')"
qry99 = "INSERT INTO comments VALUES('WHO WAS THE FIRST EMPEROR OF INDIA','RAJA RAM')"
qry100 = "INSERT INTO comments VALUES('WHO WAS THE FIRST EMPEROR OF INDIA','CHANDRAGUPTHA')"
qry101 = "INSERT INTO comments VALUES('20+(90/2) IS EQUAL TO','65')"
qry102 = "INSERT INTO comments VALUES('20+(90/2) IS EQUAL TO','65')"
qry103 = "INSERT INTO comments VALUES('WHO IS KNOWN AS THE FATHER OF INDIA','GANDHIJI')"
qry104 = "INSERT INTO comments VALUES('WHO IS KNOWN AS THE FATHER OF INDIA','MAHATMA GANDHI')"
qry105 = "INSERT INTO comments VALUES('WHAT IS THE FULLFORM OF CPU','CENTRAL PROCESSING UNIT')"
qry106 = "INSERT INTO comments VALUES('WHAT IS THE FULLFORM OF CPU','CENTRAL PROCESSING UNIT')"
qry107 = "INSERT INTO comments VALUES('AN AIR BUBBLE IN WATER WILL ACT LIKE A','CONVEX LENS')"
qry108 = "INSERT INTO comments VALUES('AN AIR BUBBLE IN WATER WILL ACT LIKE A','CONCAVE LENS')"
qry109 = "INSERT INTO comments VALUES('WHO IS KNOWN AS FATHER OF CHEMISTRY','LAVOISIER')"
qry110 = "INSERT INTO comments VALUES('WHO IS KNOWN AS FATHER OF CHEMISTRY','ANTOINE LAVOISIER')"
qry111 = "INSERT INTO comments VALUES('WHAT IS THE NEXT 2 PRIME NUMBERS AFTER 5','6,7')"
qry112 = "INSERT INTO comments VALUES('WHAT IS THE NEXT 2 PRIME NUMBERS AFTER 5','7,11')"
qry113 = "INSERT INTO comments VALUES('HOW MANY METERS ARE IN A KILOMETER','1000')"
qry114 = "INSERT INTO comments VALUES('HOW MANY METERS ARE IN A KILOMETER'.'1029')"
qry115 = "INSERT INTO comments VALUES('THE ABBREVIATION BPS STANDS FOR','BITS PER SECOND')"
qry116 = "INSERT INTO comments VALUES('THE ABBREVIATION BPS STANDS FOR','BYTES PER SECONDS')"
qry117 = "INSERT INTO comments VALUES('WHO IS THE FATHER OF PHYSICS','ISSAC NEWTON')"
qry118 = "INSERT INTO comments VALUES('WHO IS THE FATHER OF PHYSICS','ALBERT EINSTEN')"
qry119 = "INSERT INTO comments VALUES('WHO WAS THE FIRST WOMEN PRIME MINISTER OF INDIA','INDIRA GANDHI')"
qry120 = "INSERT INTO comments VALUES('WHO WAS THE FIRST WOMEN PRIME MINISTER OF INDIA','INDIRA GANDHI')"
qry121 = "INSERT INTO comments VALUES('SMALLEST UNIT OF DATA IN A COMPUTER','BIT')"
qry122 = "INSERT INTO comments VALUES('SMALLEST UNIT OF DATA IN A COMPUTER','BYTE')"
qry123 = "INSERT INTO comments VALUES('THE STRONGEST METAL ON EARTH ','TUNGESTEN')"
qry124 = "INSERT INTO comments VALUES('THE STRONGEST METAL ON EARTH','IRON')"
qry125 = "INSERT INTO comments VALUES('HOW MANY FACES DOES A CUBE HAVE','6')"
qry126 = "INSERT INTO comments VALUES('HOW MANY FACES DOES A CUBE HAVE','3')"
qry127 = "INSERT INTO comments VALUES('HOW MANY FACES DOES A CUBE HAVE','6')"
qry128 = "INSERT INTO comments VALUES('UNIT OF POWER','WATT(W)')"
qry129 = "INSERT INTO comments VALUES('UNIT OF POWER','WATT(W)')"
qry130 = "INSERT INTO comments VALUES('WHO WROTE THE INDIAN NATIONAL ANTHEM','RAVEENDRA NADH TAGORE')"
qry131 = "INSERT INTO comments VALUES('WHO WROTE THE INDIAN NATIONAL ANTHEM','RABINDRA NADH TAGORE')"
qry132 = "INSERT INTO comments VALUES('WHO WROTE THE INDIAN NATIONAL ANTHEM','RABINDRA NATH TAGORE')"
crs.execute(qry91)
crs.execute(qry92)
crs.execute(qry93)
crs.execute(qry94)
crs.execute(qry95)
crs.execute(qry96)
crs.execute(qry97)
crs.execute(qry98)
crs.execute(qry99)
crs.execute(qry100)
crs.execute(qry101)
crs.execute(qry102)
crs.execute(qry103)
crs.execute(qry104)
crs.execute(qry105)
crs.execute(qry106)
crs.execute(qry107)
crs.execute(qry108)
crs.execute(qry109)
crs.execute(qry110)
crs.execute(qry111)
crs.execute(qry112)
crs.execute(qry113)
crs.execute(qry114)
crs.execute(qry115)
crs.execute(qry116)
crs.execute(qry117)
crs.execute(qry118)
crs.execute(qry119)
crs.execute(qry120)
crs.execute(qry121)
crs.execute(qry122)
crs.execute(qry123)
crs.execute(qry124)
crs.execute(qry125)
crs.execute(qry126)
crs.execute(qry127)
crs.execute(qry128)
crs.execute(qry129)
crs.execute(qry130)
crs.execute(qry131)
crs.execute(qry132)

mydb.commit()
crs.close()


def homepage():
    while True:
        print("Enter 1 for logging into Admin panel || Enter 2 for log in as a user")
        print(""" 
                                     *****************************            ********************************            


                                                         +--------------------------------+
                                                         |           1.Admin Panel        |
                                                         +--------------------------------+         
                                                         +--------------------------------+
                                                         |           2.User               |
                                                         +--------------------------------+                                           """)
        break
    a1 = int(input("Enter your choice"))
    if a1 == 1:
        print("Admin panel")
        admin()
    elif a1 == 2:
        print("User")
        user()
    else:
        print("please enter valid choice")


def admin():
    print("Enter the password to log in to the ADMIN PANEL \n (Remember you have only 3 chances to login ) ")
    num = 1
    while num <= 3:
        a2 = int(input("Enter the password here"))
        if a2 == 1234:
            dashboard()
        print("password is incorrect")
        num = num + 1
    print(" you have no more chances")
    hp = input("Go to HOME PAGE")
    if hp == "":
        homepage()

        print(""" 
                                     *****************************     ********************************            


                                                         +--------------------------------+
                                                         |           a.Profile Mng        |
                                                         +--------------------------------+         
                                                         +--------------------------------+
                                                         |           b.Category Mng       |    |
                                                         +--------------------------------+                                         

                                                         +--------------------------------+
                                                         |           c.Comments Mng       |
                                                         +--------------------------------+      """)
        

    a1 = int(input("Enter your choice"))
    if a1 == 'a':
        print("Profile")
        profilemng()
    elif a1 == 'b':
        print("Category")
        categorymng()
    elif a1 == 'c':
        print("Comments")
        commentmng()
    else:
        print("please enter valid choice")


def profilemng():
    print(" to manage profile")
    qry06 = "SELECT * FROM profile"
    crs.execute(qry06)
    rows = crs.fetchall()
    table = PrettyTable()
    table.field_names = ["id_profile", "Username", "Email", "Followers", "Following", "Owned_Posts", "Comments"]

    for rows in rows:
        table.add_row(rows)
    print(table)
    crs.close()
    return ("")

    pr1 = input("Go back to DASHBOARD")
    if pr1 == '':
        dashboard()
    hp = input("Go to HOME PAGE")
    if hp == "":
        homepage()


def categorymng():
    print("you can add or remove any category if you want")
    print("enter the category you wanted to add ")
    print(" select the category you want to remove ")

    qry07 = "SELECT * FROM profile"
    crs.execute(qry07)
    rows = crs.fetchall()
    table = PrettyTable()
    table.field_names = ["id_profile", "Categories", "question"]


    for rows in rows:
        table.add_row(rows)
    print(table)
    crs.close()
    return ("")

    ca1 = input("Go back to DASHBOARD")
    if ca1 == '':
        dashboard()
    hp = input("Go to HOME PAGE")
    if hp == "":
        homepage()


def commentmng():
    print("comment")

    qry08 = "SELECT * FROM comments"
    crs.execute(qry08)
    rows= crs.fetchall()
    table = PrettyTable()
    table.field_names = ["question", "comment"]


    for rows in rows:
        table.add_row(rows)
    print(table)
    crs.close()
    return ("")

    co1=input("Go back to DASHBOARD")
    if co1 =='':
        dashboard()
    hp = input("Go to HOME PAGE")
    if hp == "":
        homepage()

def user():
    a3 = int(input("enter the password "))
    if a3 == 4321:
       select()
    print("You donot have an account here\n")
    act = input("Enter here to create an account")
    if act == '':
        print("\n")
    hp = input("Go to HOME PAGE")
    if hp == "":
        homepage()
    print(""" 
                                         *****************************     ********************************            


                                                             +--------------------------------+
                                                             |           a.Create             |
                                                             +--------------------------------+         
                                                             +--------------------------------+
                                                             |           b.Read               |
                                                             +--------------------------------+                                         

                                                             +--------------------------------+
                                                             |           c.Profile            |
                                                             +--------------------------------+               """) 

                                                     
                        
def select():


          print("1. create \n 2. read\n 3. Profile ")
          a5 = int(input(" enter your choice "))
          if a5 == 1:
              create()
          elif a5 == 2:
              read()
          elif a5 == 3:
              profile()
          else:
              print(" enter valid choice ")
              hp=input("Go to HOME PAGE")
          if hp == "":
              homepage()
          


def create():
    print("to create blogs")
    cr2 = input("Go back to previous page")
    if cr2 == '':
        select()
    hp1 = input("Go to HOME PAGE")
    if hp1 == "":
        homepage()


def read():
    print("to read blogs")

    qry09 = "SELECT * FROM profile"
    crs.execute(qry09)
    rows = crs.fetchall()
    table = PrettyTable()
    table.field_names = ["id_profile", "Categories", "question"]


    for rows in rows:
        table.add_row(rows)
    print(table)
    crs.close()
    return ("")

    qry10 = "SELECT * FROM comments"
    crs.execute(qry10)
    rows = crs.fetchall()
    table = PrettyTable()
    table.field_names = ["question", "comment"]

    for rows in rows:
        table.add_row(row)
    print(table)
    crs.close()
    return ("")

    re1 = input("Go back to previous page")
    if re1 == '':
        select()
    hp1 = input("Go to HOME PAGE")
    if hp1 == "":
        homepage()


def profile():
    print("profile")
    pr1 = input("Go back to previous page")
    if pr1 == '':
        select()
    hp = input("Go to HOME PAGE")
    if hp == "":
        homepage()


def dashboard():
    print("  ADMIN PANEL")
    print("_______________")
    print("DASHBOARD")
    print("\n\n")
    print(" what you wanted to manage ")
    print(" 1. Category \n 2. Profile \n 3.Commands")
    a4 = int(input("enter your choice "))
    if a4 == 1:
        categorymng()
    elif a4 == 2:
        profilemng()
    elif a4 == 3:
        commentmng()
    else:
        print(" enter valid choice ")
    hp = input("Go to HOME PAGE")
    if hp == "":
        homepage()
