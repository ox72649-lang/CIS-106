#input phase    sofia lopez 2/12/26

continuev = input("Do you want to enter employee data? (Yes to continue): ")
employeec = 0
totalgross = 0.0

#prcoess phase

while continuev == "Yes":
    lastnamev = input("Enter employee last name: ")
    hourswork = float(input("Enter hours worked: "))
    payratev = float(input("Enter rate of pay: "))

    # calculate gross pay with overtime
    if hourswork > 40:
        overtimehr = hourswork - 40
        grosspayv = (40 * payratev) + (overtimehr * payratev * 1.5)
    else:
        grosspayv = hourswork * payratev

    # update totals
    totalgross = totalgross + grosspayv
    employeec = employeec + 1

    
    # output phase (per employee) 
    # --------------------
    print("Employee Last Name:", lastnamev)
    print("Gross Pay:", grosspayv)

    # second prompt INSIDE the loop
    continuev = input("Do you want to enter another employee? (Yes to continue): ")


# final output (after loop)

if employeec > 0:
    averagepay = totalgross / employeec
else:
    averagepay = 0

print("Total Gross Pay:", totalgross)
print("Number of Employees:", employeec)
print("Average Pay:", averagepay)
