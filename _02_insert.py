
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def skill():
    """
Objective: To compute bonus of employee.
Input Parameters: None.
Return Value:skill-str value ,extra_pay-numeric value.
"""
    ch=input("Enter 1 if employee skilled or else <Enter>:")
    skill="skilled"
    if ch!= "1":
        skill="unskilled"
        bonus=0
    else:
        cha=input("Bonus :")
        if cha.isdigit()==True:
            bonus=int(round(float(cha),0))
        else:
            bonus=1000            
    return skill,bonus


#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def insert(tab_nam):
    '''
Objective: To insert the records in to table.
Input Parameters: table name string value.
Return Value: None.
'''
    import mysql.connector, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()
    from emp_calc import emp_sal ;from _functions_ import _0_modifiedDate    
    n=int(input("Enter number of records to be entered:"))
    for i in range(1,n+1):
        print("\nEnter following details of your employee;")
        L1=["Employee Id: ", "Name: ", "Sex: ", "Grade: ", "Bank account ID: ", "Mobile no.: ", "Phone no.: ","Email ID:","Basic Pay: ","Date of Birth(YYYY/MM/DD): ","Date of Joining(YYYY/MM/DD): ","Native City: ","Department: ","Designation: ","Leave Balance:"]
        a=();m=len(L1);i=0
        for j in range(0,m):            
            if j==8:
                c=input("{}".format( L1[j]))
                if c=='0':
                    c5=18000
                    c1,c2,c3,c4,c20,c6,c7,c8=emp_sal.hdg(c5)
                    c9,c10=skill()
                    c11,c12,c13,c14,c15,c16,c17,c18=emp_sal.it_pf(c5,c8,c2)
                    c19=emp_sal.tot_earn(c8,c18)+c10
                    z=(c5,c1,c2,c3,c4,c20,c6,c7,c8,c11,c12,c13,c14,c15,c16,c17,c18,c9,c10,c19)
                    a+=z
                    
                elif c.isdigit()==True or c.isdecimal()==True:
                        c5=int(round(float(c),0))
                        c1,c2,c3,c4,c20,c6,c7,c8=emp_sal.hdg(c5)
                        c9,c10=skill()
                        c11,c12,c13,c14,c15,c16,c17,c18=emp_sal.it_pf(c5,c8,c2)
                        c19=emp_sal.tot_earn(c8,c18)+c10
                        z=(c5,c1,c2,c3,c4,c20,c6,c7,c8,c11,c12,c13,c14,c15,c16,c17,c18,c9,c10,c19)
                        a+=z
                else:
                    c5=18000
                    c1,c2,c3,c4,c20,c6,c7,c8=emp_sal.hdg(c5)
                    c9,c10=skill()
                    c11,c12,c13,c14,c15,c16,c17,c18=emp_sal.it_pf(c5,c8,c2)
                    c19=emp_sal.tot_earn(c8,c18)+c10
                    z=(c5,c1,c2,c3,c4,c20,c6,c7,c8,c11,c12,c13,c14,c15,c16,c17,c18,c9,c10,c19)
                    a+=z                    
            elif j==0 or j==4 or j==14:
                c=int(input("{}".format( L1[j])))
                a+=(c,)
                
            else:
                c=input("{}".format( L1[j]))
                a+=('{}'.format(c),)
        c22=_0_modifiedDate.modifiedDate()
        a+=('{}'.format(c22),)
        str2="INSERT INTO {} \
VALUES {}"
        q3=str2.format(tab_nam,a)
        mycursor.execute(q3)
        mydb.commit()
        print(mycursor.rowcount,"RECORD INSERTED")
        i+=1
    print(i ,"TOTAL RECORD(S) INSERTED ._. ")
    mydb.close()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _  _ __ _ _ _ _ _ _ _ _


   

