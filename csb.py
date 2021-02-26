#payslip\csb.py

L2=['eCode', 'name', 'sex', 'grade', 'bank_id', 'Mobile no.' ,'Phone no.' ,'Email ID' ,'basicPay' , 'DOB', 'hireDate', 'nativeCity', 'department', 'designation', 'leave_balance']

s1="""The column names and order in your csv file must be ,
 ['eCode', 'name', 'sex', 'grade', 'bank_id',,'Mobile no.','Phone no.','Email ID', 'basicPay', 'DOB', 'hireDate', 'nativeCity', 'department', 'designation', 'leave_balance']
Important notes to be noted:
 1.The record in column 1(eCode) is NOT NULL and UNIQUE.
 2.The column must not have space.
 3.Through importing we can take records NULL but for Numeric value better to type 0 except basic pay as 0 will show error.  
 4.No repition allowed check data once.
 5.Program will show ERROR or will be terminated if not followed.
 """


from emp_calc import emp_sal
from _functions_ import _0_modifiedDate,_02_insert
import datetime

def import_csv(v):
    """
Objective: To insert records from csv file.
Input Parameters: path with filename
Return Value: None
"""
    import mysql.connector, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()


    import csv
    with open(v,'r') as newFile:
        p=csv.reader(newFile);i=0
        for row in p:
            if row==L2:
                pass
            elif row:
                print(row)
                n=len(row)
                t1=tuple(row[0:4]);c4=int(row[4])
                c5=row[5];c6=row[6]
                t1+=(c4,c5,c6,row[7]);
                c5=int(row[8])
                c1,c2,c3,c4,c20,c6,c7,c8=emp_sal.hdg(c5)
                c9,c10=_02_insert.skill()
                c11,c12,c13,c14,c15,c16,c17,c18=emp_sal.it_pf(c5,c8,c2)
                c19=emp_sal.tot_earn(c8,c18)+c10
                z=(c5,c1,c2,c3,c4,c20,c6,c7,c8,c11,c12,c13,c14,c15,c16,c17,c18,c9,c10,c19)        
                t2=()
                t2+=z
                d1,m1,y1=row[9].split('/')
                d1=int(d1);m1=int(m1);y1=int(y1)
                t="{}/{}/{}".format(y1,m1,d1)
                t3=('{}'.format(t),)
                a=()
                a=t1+t2+t3
                d1,m1,y1=row[10].split('/')
                d1=int(d1);m1=int(m1);y1=int(y1)
                t="{}/{}/{}".format(y1,m1,d1)
                t3=('{}'.format(t),)
                a+=t3
                t=tuple(row[11:n-1])
                a+=t
                c=int(row[n-1])
                a+=(c,)
                m=_0_modifiedDate.modifiedDate()
                a+=('{}'.format(m),)
                str2="INSERT INTO {} \
VALUES {}"
                tab_nam='employee'
                q3=str2.format(tab_nam,a)
                mycursor.execute(q3)
                mydb.commit()
                i+=1
        print(i,"RECORD(S) INSERTED")                
        newFile.close()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
        
def check_list():
    """
Objective: To check column and pass to insertion process.
Input Parameters: None
Return Value: None
"""

    print(s1);
    import csv
    v=input("Enter path with file_name(eg.C:/spyfiles/cs_project//a.csv):")
    with open(v,'r') as newFile:
        n=csv.reader(newFile)
        s=0
        for row in n:
            if row==L2:
                s=1
                import_csv(v)
                break
        if s==0:
            print("PLEASE READ THE BELOW IMPORTANT NOTES!!")
            check_list()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
