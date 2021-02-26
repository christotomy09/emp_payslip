# payslip\_functions_\_0_modified.py

def modifiedDate():
    """
Objective: To return updated date;time.
Input Parameters: None
Return Value: None
"""
    import datetime
    n=str(datetime.date.today())
    t=datetime.datetime.now()
    modified_date=n+";"+"{}:{}:{}".format(t.hour,t.minute,t.second)
    m=str(modified_date)
    return m
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
