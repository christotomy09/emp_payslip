#payslip/_02_pswd.py

   
def pswd():
    """
Objective: To create the database password protected.
Return value:log-str value
"""
    import _02_connect;
    import mysql.connector;a,b= _02_connect.conc_sql()
    mydb = mysql.connector.connect(host="localhost", user="{}".format(a),passwd="{}".format(b),database="c2dg")
    mycursor = mydb.cursor()

    mycursor.execute("SELECT PSWD FROM passcodes")
    p=mycursor.fetchone()
    for pswd in p:
        c1=input("Enter your password:");log="in"
        if c1==pswd:
          print("You can now access the database!!")
          pass
        else:
          print("Wrong pswd")
          log="out"
    return log
      
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
