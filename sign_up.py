#payslip/sign_up.py

from _functions_ import  _02_insert ,  _05_display, _menu_,month_tab
import _01_creation , _01_pswd_crt, csb

def sign_up():
  """
Objective : To create a database for payslip
Input parameter:None
Return value:None
"""
  _01_pswd_crt.pswd_creation()
  _01_creation.creation()
  month_tab.updates()
  print("\nYour DataBase has been sucessfully made!!\nFor no information write NULL but for numeric values just enter 0 \nPlease give input 1 for login Otherwise if you go for sign up the data will be vanished from the system")
  print("Choice\tOptions\n1.\tInsert record(s) one by one.\n2.\tInsert record(s) by importing a CSV file.")
  ch=input("Enter Choice: ")
  if ch=='1':
     _02_insert.insert("employee")
  elif ch=='2':
    csb.check_list()
  _05_display.table()
  month_tab.updates()
  _menu_.menu()
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
   
    
