#payslip\_01_pswd_crt.py


def cr_sql():
    """
Objective: To create file and store user,passwd it to connect to mysql.
Input Value: None
Return Value: None
"""
    
    f1=open("sqlid",mode='w')
    print("To connect to your mysql enter following details:") 
    user=input("\nEnter user:")
    pawd=input("Enter passwd:")
    L1=[user+" "+pawd]
    f1.writelines(L1)
    f1.close()
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def pswd_creation():
    """
Objective: To create the database password protected.
Input Value: None
Return Value: None

"""
    import _02_connect;cr_sql()
    import mysql.connector;a,b=_02_connect.conc_sql()
    mydb = mysql.connector.connect(host="localhost", user="{}".format(a),passwd="{}".format(b))
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE if exists c2dg ")
    mycursor.execute("CREATE DATABASE c2dg")
    mycursor.execute("use c2dg")
    #mycursor.execute("DROP TABLE IF EXISTS passcodes ")
    mydb.commit()
    q1="CREATE TABLE passcodes\
(user           CHAR(30),\
comp_nam  CHAR(30),\
area        CHAR(30),\
state_pin CHAR(30),\
phone  CHAR(13),\
mobile  CHAR(13),\
email    CHAR(15),\
PSWD    CHAR(8))"
    mycursor.execute(q1)
    mydb.commit()
    str2="INSERT INTO passcodes \
VALUES ('root' , '{}', '{}','{}','{}','{}','{}', '{}')"
    comp_nam=input("Company Name: ")
    print("Enter following details of your company:")
    area=input("Area(State on next input): ")
    state=input("State-pin code(LIKE DELHI-9): ")
    mobile=input("Mobile no.: ")
    phone=input("Phone no.: ")
    email=input("Email ID:")
    c1=input("Enter the pswd(8 characters):")
    c2=input("Renter the pswd:")
    if c1==c2:
        mycursor.execute(str2.format(comp_nam, area, state,mobile,phone,email, c1))
        mydb.commit()
    else:
      print("Not Matching,Try again!!")
      pswd_creation()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    

