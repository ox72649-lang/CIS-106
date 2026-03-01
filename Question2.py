#input phase    sofia lopez 2/12/26

startvalue = int(input("Enter the start value: "))
stopvalue = int(input("Enter the stop value: "))
incrementv = int(input("Enter the increment value: "))

currentnum = startvalue
loopcontrol = True
iterationc = 0

# process phase

while loopcontrol:
    if currentnum > stopvalue:
        loopcontrol = False
    else:
       
        # output phase
        
        print(currentnum)
        currentnum = currentnum + incrementv
        iterationc = iterationc + 1
