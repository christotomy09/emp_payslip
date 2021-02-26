def export_csv(v):
    import mysql.connector,csv, _02_connect;a,b=_02_connect.conc_sql()
    mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()
    m=["Emp_ID", "Name","Sex","Grade","Bank Account No.", "Mobile","Phone","Email ID","Basic Pay","HRA","DA","CA","TA","Ration Allowance","Risk Allowance", "Washing Allowance","Gross Salary", "IncomeTax","PF","House Loan" ,"Car Loan","Medical Insurance", "Life Insurance", "Pension Contribution" ,"DED","Skill", "Bonus","Net Salary","DOB", "Hiredate","Native City","Department","Designation","Leave Balance", "Modified datetime"]
    with open("C:/Users/best/Documents//{}".format(v),"w") as newFile:
        f1=csv.writer(newFile)
        f1.writerow(m)
        mycursor.execute("SELECT * FROM employee")
        records=mycursor.fetchall()
        for row in records:
            f1.writerow(list(row))
        
