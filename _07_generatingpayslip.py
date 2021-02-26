# payslip\_functions_\_07_generatingpayslip.py


def month_name(n):
    if n==1:
        month="January"
    elif n==2:
        month="February"
    elif n==3:
        month="March"
    elif n==4:
        month="April"
    elif n==5:
        month="May"
    elif n==6:
        month="June"
    elif n==7:
        month="July"
    elif n==8:
        month="August"
    elif n==9:
        month="September"
    elif n==10:
        month="October"
    elif n==11:
        month="November"
    elif n==12:
        month="December"
    return month



def write(file,tab_nam,eCode,m,y):
    """
Objective:To write the payslip on a given file.
Input Parameters: file string value,eCode integer value.
Return Value:None
"""
    import mysql.connector, datetime, _02_connect;a,b=_02_connect.conc_sql();c,d,e,f=tab_nam,eCode,m,y
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()   
    f1=open("C:/Users/best/Downloads//{}".format(file),"w")
    mycursor.execute("SELECT comp_nam, area, state_pin, phone, mobile, email FROM passcodes")
    comp,a, state_pin, phone, mobile, email=mycursor.fetchone();print(comp,a, state_pin, phone, mobile, email)
    #mycursor.execute("SELECT * FROM {} where eCode={}".format(c,d))
    f1.writelines(["\n"+"  "*31+"{}".format(comp)+"  "*31])
    f1.writelines(["\n"+"  "*29+"{}".format(a)+"  "*29])
    f1.writelines(["\n"+"  "*33+"{}".format(state_pin)+"  "*33])
    f1.writelines(["\n"+"  "*20+"Payslip for the period of {} {}".format(month_name(m),y)+"  "*20])
    f1.writelines(["\n"+"  "*50+"Ph:{}, Mobile:{}".format(phone,mobile)])
    f1.writelines(["\n"+"  "*50+"email:{}".format(email)])
    t=datetime.date.today()
    t1=str(t)
    f1.writelines(["\n"+'  '*50+"Date:{}".format(t1)])
    f1.writelines(["\n"+'= '*66])
    L5=["Employee ID: ", "Name: ", "Mobile: ", "Phone: ", "Native City: ","Email ID:", "Sex: ", "Grade: ", "Date of Birth: ", "Date of Joining: " ,"Bank ID: ", "Department: ", "Designation: ","Leave Balance:"]
    mycursor.execute("SELECT eCode, name, mobile, Phone, nativeCity, email, sex, grade,  DOB, hireDate, bank_id, department, designation, leave_balance, basicPay, HRA, DA, CA, TA, rationAllowance, riskAllowance, washingAllowance, grossSalary, incomeTax, PF, houseLoan, carLoan, medicalInsurance , lifeInsurance, pensionContribution , DED FROM {} where eCode={}".format(tab_nam,eCode))
    
    records=mycursor.fetchone();
    #print(records)
    records1=records[0:14];records2=records[14:23];records3=records[23:31]
    f1.writelines(["\n"])
    for i in range(0,len(L5)):
        if i==0 or i==4:
            f1.writelines(["{}".format(L5[i])+"{}".format(records1[i])+"\t\t\t\t"])
            if i%2!=0:
                    f1writelines(["\n"])
        elif i==6:
            f1.writelines(["{}".format(L5[i])+"{}".format(records1[i])+"\t\t\t\t\t"])
            if i%2!=0:
                f1.writelines(["\n"])
            
        elif i!=6 or i!=0 or i!=4:
                f1.writelines(["{}".format(L5[i])+"{}".format(records1[i])+"\t\t\t"])
                if i%2!=0:
                    f1.writelines(["\n"])
    f1.writelines(["\n"+'= '*66])
    f1.writelines(["\n"+"SALARY UNDER CATEGORY-WISE\n"])
    f1.writelines(["\n"+"SALARY\t\t\t\t\t\t\tAmount(Rs.)\n"])
    L6=["EARN", "Basic Pay", "HRA\t", "DA\t", "City Allowance", "Travel Allowance", "Ration Allowance", "Risk Allowance", "Washing Allowance","GROSS SALARY", "DEDUCTION", "Income Tax", "PF\t","House Loan", "Car Loan\t", "Medical Insurance","Life Insurance" ,"Pension Contribution"  ,"TOTAL DEDUCTED"];b=0
    for j in range(0,len(L6)):
        if j==0 or j==10:
            f1.writelines(["\n"+"{}".format(L6[j])+"\n\n"])
        elif j==11 or j==12 or j==13 or j==14 or j==15 or j==16 or j==17:
            f1.writelines(["\n"+"{}".format(L6[j])+"\t\t\t\t\t\t"+"{}".format(records3[b])])
            b+=1
        elif j==9:
            f1.writelines(["\n"+"\t"*5+"{}".format(L6[j])+":\t"+"{}".format(records2[j-1])])
        elif j==18:
            f1.writelines(["\n"+"\t"*4+"          {}".format(L6[j])+": \t"+"{}".format(records3[b])])
        elif j==1:
            f1.writelines(["\n"+"{}".format(L6[j])+"\t\t\t\t\t\t"+"{}".format(records2[j-1])])
        elif j==8:
            f1.writelines(["\n"+"{}".format(L6[j])+"\t\t\t\t\t"+"{}".format(records2[j-1])])
        elif j==17:
            f1.writelines(["\n"+"{}".format(L6[j])+"\t\t\t\t\t\t"+"{}".format(records3[b])])
            b+=1
        else:
            f1.writelines(["\n"+"{}".format(L6[j])+"\t\t\t\t\t\t"+"{}".format(records2[j-1])])
    f1.writelines(["\n"+'='*78+"\n"])
    mycursor.execute("SELECT bonus,net_salary FROM {} where eCode={}".format(tab_nam,eCode))
    c13,c14=mycursor.fetchone()
    f1.writelines(["\n"+"\t\t\t\t\t\t"+"BONUS: {}".format(c13)])
    f1.writelines(["\n"+"\n"+'  '*30+"Net Salary(TOTAL EARN+TOTAL DEDUCTION+BONUS):{}".format(c14)])
    f1.writelines(["\n"+"\n"+"(Sales Manager)"])
    f1.close()
    mydb.commit()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
def payslip():
    """
Objective:To display the payslip on a given file.
Input Parameters: None
Return Value:None
"""
    import mysql.connector, datetime, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()   
    eCode=int(input("Enter your employee code:"))
    m=int(input("Enter month:"));y=int(input("Enter year:"))
    tab_nam="emp_{}_{}".format(m,y)
    mycursor.execute("SELECT comp_nam, area, state_pin, phone, mobile, email FROM passcodes")
    comp,a, state_pin, phone, mobile, email=mycursor.fetchone()
    mycursor.execute("SELECT * FROM {} where eCode={}".format(tab_nam,eCode))
    if mycursor.fetchall()!=[]:
        print("\n"+"  "*31,"{}".format(comp),"  "*31)
        print("  "*29,"{}".format(a),"  "*29)
        print("  "*33,"{}".format(state_pin),"  "*33)
        print("  "*20,"Payslip for the period of {} {}".format(month_name(m),y),"  "*20)
        print("  "*50,"Ph:{}, Mobile:{}".format(phone,mobile))
        print("  "*50,"email:{}".format(email))
        t=datetime.date.today();t1=str(t)
        print('  '*50,"Date:{}".format(t1))
        print('= '*66)
        L5=["Employee ID: ", "Name: ", "Mobile: ", "Phone: ", "Native City: ","Email ID:", "Sex: ", "Grade: ", "Date of Birth: ", "Date of Joining: " ,"Bank ID: ", "Department: ", "Designation: ","Leave Balance"]
        mycursor.execute("SELECT eCode, name, mobile, Phone, nativeCity, email, sex, grade,  DOB, hireDate, bank_id, department, designation, leave_balance, basicPay, HRA, DA, CA, TA, rationAllowance, riskAllowance, washingAllowance, grossSalary, incomeTax, PF, houseLoan, carLoan, medicalInsurance , lifeInsurance, pensionContribution , DED FROM {} where eCode={}".format(tab_nam,eCode))
        records=mycursor.fetchone();records1=records[0:14];records2=records[14:23];records3=records[23:31]
        for i in range(0,len(L5)):
            if i==0 or i==4:
                print("{}".format(L5[i]),records1[i],end="\t\t\t\t")
                if i%2!=0:
                        print("\n")
            elif i==6:
                print("{}".format(L5[i]),records1[i],end="\t\t\t\t\t")
                if i%2!=0:
                    print("\n")
                
            elif i!=6 or i!=0 or i!=4:
                    print("{}".format(L5[i]),records1[i],end="\t\t\t")
                    if i%2!=0:
                        print("\n")
        print("\n"+'= '*66)
        print("SALARY UNDER CATEGORY-WISE\n")
        print("SALARY\t\t\t\t\t\t\tAmount(Rs.)\n")
        L6=["EARN", "Basic Pay", "HRA\t", "DA\t", "City Allowance", "Travel Allowance", "Ration Allowance", "Risk Allowance", "Washing Allowance","GROSS SALARY", "DEDUCTION", "Income Tax", "PF\t","House Loan", "Car Loan\t", "Medical Insurance","Life Insurance" ,"Pension Contribution"  ,"TOTAL DEDUCTED"];b=0
        for j in range(0,len(L6)):
            if j==0 or j==10:
                print("{}".format(L6[j]),end="\n\n")
            elif j==11 or j==12 or j==13 or j==14 or j==15 or j==16 or j==17:
                print("{}".format(L6[j]),records3[b],sep="\t\t\t\t\t\t")
                b+=1
            elif j==9:
                print("\t"*5+"{}".format(L6[j]),records2[j-1],sep=":\t")
            elif j==18:
                print("\t"*4+"          {}".format(L6[j]),records3[b],sep=": \t")
            elif j==1:
                print("{}".format(L6[j]),records2[j-1],sep="\t\t\t\t\t\t")
            elif j==8:
                print("{}".format(L6[j]),records2[j-1],sep="\t\t\t\t\t")
            elif j==17:
                print("{}".format(L6[j]),records3[b],sep="\t\t\t\t\t\t")
                b+=1
            else:
                print("{}".format(L6[j]),records2[j-1],sep="\t\t\t\t\t\t")
        mycursor.execute("SELECT bonus ,net_salary FROM {} where eCode={}".format(tab_nam,eCode))
        c13,c14=mycursor.fetchone()
        print("\t\t\t\t\t\t"+"BONUS: {}".format(c13))
        print("\n"+'  '*10+"Net Salary(TOTAL EARN+TOTAL DEDUCTION+BONUS):{}".format(c14))
        print("\n(Sales Manager)\n")
        mydb.commit()
        x=input("Do you want write copy of this payslip as text file?(Yes/NO): ")
        if x=="Yes" or x=="yes" or x=="YES":
            file=input("Enter file name(eg.\"emp_01.txt\"):")
            write(file,tab_nam,eCode,m,y)
            print("Sucessfully made a copy in \"C:/Users/best/Downloads\"!!")
        else:
            mydb.commit()
    else:
        print("Given Data Does Not Exist")
#payslip()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
