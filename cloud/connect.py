# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:58:50 2023

@author: Shivani_SB
"""
def showall():
    sql= "SELECT * from LOGIN"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Username is : ",  dictionary["USERNAME"])
        print("The Password is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(username,password):
    sql= "select * from USER where username='{}' and password='{}'".format(username,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
       print("The Username is : ",  dictionary["USERNAME"])
        print("The Password is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,username,password):
    sql= "INSERT into LOGIN VALUES('{}','{}','{}','{}','{}','{}','{}')".format(username,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud","PORT": 32286 SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=nmb64903;PWD=PGE9ynL5hzFRvf7i",'','')
    print(conn)
    print("connection successful...")
    #insertdb(conn,"Hari","Hari@gmail.com",'1234567890','Adarsh nagar','Faculty','Civil','1234567')
    #getdetails("Hari@gmail.com",'1234567')
    #showall()

except:
    print("Error connecting to the database")



