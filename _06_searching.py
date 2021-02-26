# payslip\_functions_\_06_searching.py


def search_1(eCode):
    
    """
Objective: To traverse the Searched Record.
Input Parameters: Employee code - numeric value
Return Value: None
"""
    import mysql.connector, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()

    print("\n")
    mycursor.execute("SELECT eCode, name, sex, grade, DOB, hireDate, bank_id, mobile, Phone, email ,nativeCity, leave_balance, basicPay, HRA, DA, CA, TA, rationAllowance, riskAllowance, washingAllowance,grossSalary, incomeTax, PF, houseLoan, carLoan, medicalInsurance , lifeInsurance, pensionContribution, DED, bonus, net_salary  FROM employee where eCode={}".format(eCode))  

    L1=["Emp. Code: ", "Name: ", "Sex: ", "Grade: ","Date of birth: ","Date of Joining: ","Bank ID: ", "Mobile no.: ", "Phone no.: ","Email ID:", "Native City: ","Leave Balance: ","Basic Pay: ","HRA: ","DA: ", "City Allowance: ", "Travel Allowance: ", "Ration Allowance: ", "Risk Allowance: ", "Washing Allowance: ","EARN: ","ITR: ","PF: ","DED: ","House Loan: ", "Car Loan: ", "Medical Insurance:","Life Insurance:" ,"Pension Contribution:" ,"BONUS:", "Net Pay: "]
    n=mycursor.fetchall();i=0
    for m in n:
        for j in m:
            print(L1[i],j,end=" \t ")
            i+=1
            if i%2==0:
                print("\n")
            pass
        pass
    mydb.commit()


#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
def search_2():
    """
Objective: To Search Record by a given choice.
Input Parameters: None
Return Value: None
"""
    import mysql.connector, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()

    while True:
        print("\nChoice\tTo search by\n1.\teCode\n2.\tName\n3. \tNative City\n4. \tTo exit")
        ch=input("Enter choice: ")
        if ch=="1":
            eCode=int(input("Enter your employee code: "))
            mycursor.execute("SELECT * FROM employee where eCode = {} ".format(eCode))
            if mycursor.fetchall()!=[]:
                search_1(eCode)
            else:
                print("Data given don't exist!!")
        elif ch=="2":
            name=input("Enter name: ")
            mycursor.execute("SELECT * FROM employee where name LIKE '{}' or name LIKE '{}%' or name LIKE '%{}' or name LIKE '%{}%'  ".format(name, name, name, name))
            if mycursor.fetchall()!=[]:
                mycursor.execute("SELECT * FROM employee where name LIKE '{}' or name LIKE '{}%' or name LIKE '%{}' or name LIKE '%{}%'  ".format(name, name, name, name))
                n=mycursor.fetchall()
                for row in n:
                        search_1(row[0])
            else:
                print("Data given don't exist!!")
        elif ch=="3":
            city=input("Enter Native City: ")
            mycursor.execute("SELECT * FROM employee where nativeCity LIKE '{}' or nativeCity LIKE '{}%' or nativeCity LIKE '%{}' or nativeCity LIKE '%{}%' ".format(city, city, city, city))
            if mycursor.fetchall()!=[]:
                mycursor.execute("SELECT * FROM employee where nativeCity LIKE '{}' or nativeCity LIKE '{}%' or nativeCity LIKE '%{}' or nativeCity LIKE '%{}%'  ".format(city, city, city, city))
                n=mycursor.fetchall()
                for row in n:
                        search_1(row[0])
            else:
                print("Data given don't exist!!")          
        else:
            break
        mydb.commit()
        
            
                
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
