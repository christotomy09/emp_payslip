#payslip\login.py

from _functions_ import  _menu_,month_tab
import  _02_pswd , _02_connect

def login():
  """
Objective : To acess the database of payslip
Input parameter:None
Return value:None
"""
  month_tab.updates()
  if _02_pswd.pswd()=="in":
    _menu_.menu()
  else:
    login()
 
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
