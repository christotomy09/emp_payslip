# payslip\_functions_\_04_delete.py


def del_record():
    '''
Objective: To delete the records in the table.
Input Parameters: Table name string value
Return Value: None
'''
    import mysql.connector, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()
    n=int(input("Enter number of records to be deleted:"));i=0
    for i in range(0,n):     
        str3="DELETE FROM  employee WHERE  eCode={}"
        m=int(input("Enter employee code of employee to be deleted:"))        
        q4=str3.format(m)
        mycursor.execute(q4)
        mydb.commit()
        print(mycursor.rowcount,"RECORD DELETED")
    print(i,"TOTAL RECORD(s) DELETED")
    mydb.close()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _  _ __ _ _ _ _ _ _ _ _
