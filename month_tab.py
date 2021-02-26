# payslip\_functions_\month_tab.py

import datetime

def date():
    t=datetime.date.today()
    y=t.year
    m=t.month
    return m,y

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def cr_table_mm_yy():
    import mysql.connector, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()

    m,y=date()
    tab_nam="emp_{}_{}".format(m,y)
    q2="CREATE TABLE {} AS SELECT*FROM employee".format(tab_nam)
    mycursor.execute(q2)
    mydb.commit()
    mydb.close()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
def up_table_mm_yy():
    import mysql.connector, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()

    m,y=date()
    tab_nam="emp_{}_{}".format(m,y)
    mycursor.execute("DROP TABLE IF EXISTS {} ".format(tab_nam))
    mydb.commit()
    q2="CREATE TABLE {} AS SELECT*FROM employee".format(tab_nam)
    mycursor.execute(q2)
    mydb.commit()
    mydb.close()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def updates():
    n=datetime.date.today()
    y=n.year
    m=n.month
    t=datetime.date(y, m, 1)
    if n==t:
        cr_table_mm_yy()
    else:
        up_table_mm_yy()
    

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
