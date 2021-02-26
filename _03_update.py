# payslip\_functions_\_03_update.py


def edit():
    """
Objective: To edit the records of given employee id
Input Parameter: None
Return Value: None
"""
    import mysql.connector, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor();b=0
    from emp_calc import emp_sal;from _functions_ import _02_insert, _0_modifiedDate;m=_0_modifiedDate.modifiedDate()
    o=int(input("Enter employee code of employee to be edited:"))
    while True:
        print("Choice\tColumn")
        print("1\tName \n2\tSex  \n3\tGrade  \n4\tb_pay(to change bonus) \n5\tDate of Birth \n6\tDate of Joining  \n7\tNative  \n8\tDept.  \n9\tDesignation \n10\tLeave Balance\n11\tBank ID\n12\tMobile No.\n13\tPhone no.\n14\tEmail ID")
        ch=input("Enter your choice(to exit <Enter>):");str5=''
        if ch=='1':
            c2=input("Name: ")
            str5+=' name =  \'{}\''.format(c2)
            str5+=',';b+=1
        elif ch=='2':
            c3=input("Sex: ")
            str5+=' sex = \'{}\''.format(c3)
            str5+=',';b+=1
        elif ch=='3':
            c4=input("Grade: ")
            str5+=' grade = \'{}\''.format(c4)
            str5+=',';b+=1
        elif ch=='11':
            c21=input("Bank account no.:")
            str5+=' bank_id = \'{}\''.format(c21)
            str5+=',';b+=1
        elif ch=='4':
            c=input("Basic Pay: ")
            if c==0:
                
                c5=18000
                c1,c2,c3,c4,c20,c6,c7,c8=emp_sal.hdg(c5)
                c9,c10=_02_insert.skill()
                c11,c12,c13,c14,c15,c16,c17,c18=emp_sal.it_pf(c5,c8,c2)
                c19=emp_sal.tot_earn(c8,c18)+c10
                
            elif c.isdigit()==False or c.isdecimal()==False:
                
                c5=18000
                c1,c2,c3,c4,c20,c6,c7,c8=emp_sal.hdg(c5)
                c9,c10=_02_insert.skill()
                c11,c12,c13,c14,c15,c16,c17,c18=emp_sal.it_pf(c5,c8,c2)
                c19=emp_sal.tot_earn(c8,c18)+c10
                
            elif c.isdigit()==True or c.isdecimal()==True:
                
                c5=int(round(float(c),0))
                c1,c2,c3,c4,c20,c6,c7,c8=emp_sal.hdg(c5)
                c9,c10=_02_insert.skill()
                c11,c12,c13,c14,c15,c16,c17,c18=emp_sal.it_pf(c5,c8,c2)
                c19=emp_sal.tot_earn(c8,c18)+c10

            str5+=' basicPay ={}, HRA = {}, DA = {},CA={},TA={}, grossSalary={}, incomeTax ={}, PF={},houseLoan={}, carLoan={}, medicalInsurance={}, lifeInsurance={},pensionContribution={}, DED={}, skill=\'{}\', bonus={}, net_salary={}'.format(c5,c1,c2,c3,c4,c8,c11,c12,c13,c14,c15,c16,c17,c18,c9,c10,c19)
            str5+=',';b+=1
        elif ch=='5':
            c15=input("Date of Birth(YYYY/MM/DD):")
            str5+=' DOB = \'{}\''.format(c15)
            str5+=',';b+=1
        elif ch=='6':
            c16=input("Date of Joining(YYYY/MM/DD): ")
            str5='hireDate = \'{}\''.format(c16)
            str5+=',';b+=1
        elif ch=='7':
            c17=input("Native City: ")
            str5+='nativeCity = \'{}\''.format(c17)
            str5+=',';b+=1
        elif ch=='8':
            c18=input("Department: ")
            str5+='department  = \'{}\''.format(c18)
            str5+=',';b+=1
        elif ch=='9':
            c19=input("Designation: ")
            str5+='designation = \'{}\''.format(c19)
            str5+=',';b+=1
        elif ch=='10':
            c20=input("Leave Balance: ")
            str5+='leave_balance = \'{}\''.format(c20)
            str5+=',';b+=1
        elif ch=='12':
            c20=input("Mobile No.: ")
            str5+='mobile = \'{}\''.format(c20)
            str5+=',';b+=1
        elif ch=='13':
            c20=input("Phone no.: ")
            str5+='Phone = \'{}\''.format(c20)
            str5+=',';b+=1
        elif ch=='14':
            c20=input("Email id: ")
            str5+='email = \'{}\''.format(c20)
            str5+=',';b+=1
        else:
            break
        mycursor.execute("UPDATE employee set {} modified_datetime='{}' where eCode={}".format(str5, m, o))
        print(mycursor.rowcount,"RECORD UPDATED ._.")
    mydb.commit()
    mydb.close()
        
    
#_ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
