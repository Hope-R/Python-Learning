work_hours = [("Rajeev",100),("ABC",120),("XYZ",130)]

# Find the employee of the month - Judge by number of hours worked

def employee_check(work_hours):

    # Set some max value to initially beat, like 0
    current_max = 0
    # Set a blank employee name corresponding to the current_max
    employee_of_month = ""

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month,current_max)

e = employee_check(work_hours)
print(e)
