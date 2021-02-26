
def hdg(basic_salary):
    """
Objective: To compute a HRA, DA, CA, TA, Gross Salary
Input parameter: Basic Salary integer value
Return Value: HRA, DA, CA, TA, Ration Allowance, Risk Allowance, Washing Allowance Gross Salary - numeric value
"""
    if basic_salary<60000:
        HRA=0.20*basic_salary
        DA=0.80*basic_salary

    else:
        if basic_salary>=60000:
            HRA=22000.0
            DA=0.9*basic_salary
    CA=0.01*basic_salary;TA=0.005*basic_salary
    ration_allowance=1500;risk_allowance=2500;washing_allowance=1750
    gross_salary = basic_salary+HRA+DA+CA+TA+ration_allowance+risk_allowance+washing_allowance
    return HRA, DA, CA, TA, ration_allowance, risk_allowance, washing_allowance, gross_salary

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def it_pf(basic_salary, gross_salary, DA):
    """
Objective: To compute a tax,  House Loan,  Medical Insurance, Life Insurance, PF, Deduction
Input parameter:Basic Salary, gross_salary, DA integer value
Return Value:tax, House Loan, Car Loan, Medical Insurance, Life Insurance, PF,Pension Contribution, DED - numeric value
"""
    
    if 12*gross_salary<=250000:
        tax+=0.0
    elif 12*gross_salary<=500000:
        tax=0.0+(12*gross_salary-250000)*0.10
    elif 12*gross_salary<=1000000:
        tax=0.0+25000+(12*gross_salary-500000)*0.20
    elif 12*gross_salary>1000000:
        tax=0.0+25000+100000+(12*gross_salary-1000000)*0.30
    tax=round(tax/12.0,0)
    if basic_salary<15000:
        PF=0.07*(basic_salary+DA)
    else:
        if basic_salary>=15000:
            PF=0.12*(basic_salary+DA)
    ch1=input("Enter 1 if employee have taken Loan or else <Enter>: ")
    if ch1=="1":
        car_loan=4500;houseLoan=0.05*basic_salary;
    else:
        car_loan=houseLoan=0
    ch2=input("Enter 1 if employee have taken any insurance or else<Enter>: ")
    if ch2=="1":
        medicalInsurance=0.05*basic_salary;lifeInsurance=0.03*basic_salary
    else:
        medicalInsurance=lifeInsurance=0
    pensionContribution=0.0075*basic_salary
    DED=tax+PF+houseLoan+car_loan+medicalInsurance+lifeInsurance
    return tax, PF, houseLoan, car_loan, medicalInsurance, lifeInsurance,pensionContribution, DED

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def tot_earn(gross_salary,DED):
    """
Objective: To compute a total salary
Input parameter: Gross Salary, Deducion integer value
Return Value: tot_salary - numeric value
"""
    tot_salary=gross_salary-DED
    return tot_salary

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _  _ __ _ _ _ _ _ _ _ _
