# Get the amount of hours spent by user
hr = input("Enter hours: ")
# try and except condition
try:
    new_hr = float(hr)
except:
    new_hr = 0

# Get the rate to be applied
rt = input("Enter Rate: ")
# try and except condition
try:
    new_rt = float(rt)
except:
    new_rt = -1

# get an if statement for the above condition
if (float(new_hr) > 0 and float(new_rt) > 0):
    print ("Input format correct")

else:
    print ("Error!, Please enter Hours and Rate in digits")

# Define the functions
def Regular_pay(Hours, Rate):
    reg_pay = float(Hours) * float(Rate)
    return reg_pay

def Overtime_Pay(Hours, Rate):
    reg_pay = float(Hours) * float(Rate)
    Added_Pay = (float(Hours) - 40) * (float(Rate) * 1.5)
    Over_pay = reg_pay + Added_Pay
    return Over_pay

# call the functions Regular_pay and Overtime_Pay
Regular = Regular_pay(new_hr, new_rt)

Overtime = Overtime_Pay(new_hr, new_rt)

# Get gross pay value if hours is below  0
if float(new_hr) <= 0 :
    print ("Wrong hour value")

# Get gross pay value if rate is below  0
if float(new_rt) <= 0 :
    print ("Wrong rate value")

# Get gross pay value if hours is below 40
elif 0 < float(new_hr) <= 40 :
    Regular = Regular_pay(new_hr, new_rt)
    print ("Regular Pay:", str(Regular) + " naira")

# Get gross pay value if hours is above 40
elif float(new_hr) > 40 :
    Overtime = Overtime_Pay(new_hr, new_rt)
    print ("Overtime Pay:", str(Overtime) + " naira")
