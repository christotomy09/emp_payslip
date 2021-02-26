# payslip\_functions_\_menu_.py

from _functions_ import   _02_insert, _03_update,  _04_delete,  _05_display,  _06_searching, _07_generatingpayslip, month_tab

def menu():
  """
Objective: To access functions with payslip system.
Input Parameters: None
Return Value: None
"""
  import mysql.connector, _02_connect,csa,csb,_01_creation,_02_pswd;a,b=_02_connect.conc_sql()
  mydb=mysql.connector.connect(host= "localhost", user="{}".format(a), passwd="{}".format(b),database="c2dg")
  mycursor = mydb.cursor()


  while True:
    print('\nMAIN MENU')
    print('Press 1 for Inserting Data ')
    print('Press 2 for Editing Data')
    print('Press 3 for Deleting Data')
    print('Press 4 for Displaying Data')
    print('Press 5 for Searching Data')
    print('Press 6 for Report Generating')
    print('Press 7 for Exporting Data as CSV')
    print('Press 8 for Quit')
    choice = input('What would you like press: ')
    if choice == '1':
      print("Choice\tOptions\n1.\tInsert record(s) one by one.\n2.\tInsert record(s) by importing a CSV file.")
      ch=input("Enter Choice: ")
      if ch=='1':
        _02_insert.insert("employee")
      elif ch=='2':
        csb.check_list()
      month_tab.updates()
    elif choice == '2':
      _03_update.edit()
      month_tab.updates()
    elif choice == '3':
      print("Choice\tOptions\n1.\tDelete record(s) one by one.\n2.\tDrop the Table and Create New.")
      ch=input("Enter Choice: ")
      if ch=='1':
        _04_delete.del_record()
        month_tab.updates()
      elif ch=='2':
        if _02_pswd.pswd()=="in":
          mycursor.execute("Drop Table employee")
          _01_creation.creation()
          mydb.commit()
        else:
          print("\nTry again for choice 3 ,then choice 2")        
      elif ch=='3':
        mycursor.execute("Drop Table employee")
        _01_creation.creation()
    elif choice == '4':
      _05_display.table()
      month_tab.updates()
    elif choice == '5':
      _06_searching.search_2()
      month_tab.updates()
    elif choice == '6':
      _07_generatingpayslip.payslip()
      month_tab.updates()
    elif choice=='7':
      v=input("CSV file name:")
      csa.export_csv(v)
    elif choice not in ['1','2','3','4','4','5','6','7' ]:
      break
    mydb.close()
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
      
