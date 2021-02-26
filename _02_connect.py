#payslip\_02_connect.py

def conc_sql():
    f1=open("sqlid",mode='r')
    n=f1.readlines()
    for i in n:
        a,b=i.split()
        f1.close()
    return a,b
 #_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   

def connect():
    import mysql.connector;a,b=conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
