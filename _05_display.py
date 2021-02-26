# payslip\_functions_\_04_delete.py

def table():
    """
Objective: To display the whole database.
Input parameters: None
Return Value: None
"""
    
    import mysql.connector, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT eCode, name, sex, grade, bank_id, mobile, Phone, email, DOB,hireDate  FROM employee")
    records=mycursor.fetchall()
    print("Emp Id \tName \tSex \tGrade \tBank Account No.  \tMobile Number \tPhone Number \tEmail ID \t\tDate of Birth\tHire date")
    for row in records:
        for col in row:
            print(col, end='\t')
        print()
    mydb.commit()
    mycursor.execute("SELECT eCode, nativeCity, department,designation,leave_balance, modified_datetime  FROM employee")
    records3=mycursor.fetchall()
    print("\nemp_Id\t City\tDepart.\tDes.\tLeave Bal. Last updated(Date;time)")
    for row in records3:
        for col in row:
            print(col, end='\t')
        print()
    mydb.commit()
    mycursor.execute("SELECT eCode, basicPay, HRA, DA, CA, TA, rationAllowance, riskAllowance, washingAllowance, grossSalary, incomeTax, PF, houseLoan, carLoan, medicalInsurance, lifeInsurance, pensionContribution, DED, skill, bonus, net_salary FROM employee")
    records1=mycursor.fetchall()
    print("\nEmp. Id\t b_pay \tHRA \tDA \tCA \tTA\tRA\tR&H\twashing\t EARN\t ITR \tPF\thouseLoan carLoan med_Ins lifeIns Pension\tDED\tskill\tbonus   net_salary")
    for row in records1:
        for col in row:
            print(col, end='\t')
        print()
    mydb.commit()
        



#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _  _ __ _ _ _ _ _ _ _ _

       
       
