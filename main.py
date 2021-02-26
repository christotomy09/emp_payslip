#payslip\main.py

##################### FUNCTION DEFINITIONS ARE OVER #######################
#__main__ Starts__From__Here

import login, sign_up
print("Choice\tOptions")
print("0\tSign up")
print("1\tLogin")
ch=input("Enter the choice (or to exit else just <Enter>):")
if ch=='0':
    sign_up.sign_up()
elif ch=='1':
    login.login()
else:
    pass
    
"""
ABC Private Ltd.,
Enter following details of your company:
Area(State on next input): 54/10, Street No.-15
State-pin code(LIKE DELHI-9): Delhi-110007
Mobile no.: 98542 38724
Phone no.: 01123456761
Email ID:ABC@gmail.com
"""


