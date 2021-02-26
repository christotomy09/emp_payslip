#payslip\_01_creation.py

   
def creation():
    """
Objective: To create database with python-mySql interface

"""
    import _02_connect;
    import mysql.connector;a,b= _02_connect.conc_sql()
    mydb = mysql.connector.connect(host="localhost", user="{}".format(a),passwd="{}".format(b))
    mycursor = mydb.cursor()

    mycursor.execute("use c2dg")
    tab_nam="employee"
    q1="CREATE TABLE {} \
(eCode     INTEGER NOT NULL UNIQUE PRIMARY KEY,\
name    CHAR(30) NOT NULL,\
sex            CHAR(1),\
grade       CHAR(2),\
bank_id CHAR(30),\
mobile  CHAR(13),\
Phone CHAR(13),\
email   CHAR(30),\
basicPay       DECIMAL(10,0),\
HRA       DECIMAL(10,0),\
DA       DECIMAL(10,0),\
CA     DECIMAL(10,0),\
TA      DECIMAL(10,0),\
rationAllowance       DECIMAL(10,0),\
riskAllowance       DECIMAL(10,0),\
washingAllowance       DECIMAL(10,0),\
grossSalary       DECIMAL(10,0),\
incomeTax       DECIMAL(10,0),\
PF       DECIMAL(10,0),\
houseLoan      DECIMAL(10,0),\
carLoan       DECIMAL(10,0),\
medicalInsurance       DECIMAL(10,0),\
lifeInsurance       DECIMAL(10,0),\
pensionContribution       DECIMAL(10,0),\
DED       DECIMAL(10,0),\
skill        CHAR(30),\
bonus     DECIMAL(10,0),\
net_salary  DECIMAL(10,0),\
DOB        DATE CHECK(DOB LIKE '----/--/--'),\
hireDate   DATE CHECK(hireDate LIKE '----/--/--'),\
nativeCity CHAR(30),\
department CHAR(30),\
designation CHAR(30),\
leave_balance INTEGER(3),\
modified_datetime CHAR(30)\
);"
    mycursor.execute(q1.format(tab_nam))
    mydb.commit()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

