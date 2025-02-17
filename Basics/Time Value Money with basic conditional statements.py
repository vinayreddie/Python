import numpy as np

Historical_Returns = []
totalReturns = []
InitialInvestment = float(input("enter initial investment:"))
return_period = int(input("enter return period:"))

for i in range(1,return_period+1):  

 yoyreturn = float(input(f"enter {i} - Year return:") )
 Historical_Returns.append(yoyreturn)
 
 
Present_Value = InitialInvestment
for i in Historical_Returns[:return_period+1]:
   Future_Value = Present_Value * (1+i/100)
   Present_Value = Future_Value
   totalReturns.append(round(Future_Value,2))

averageReturn = float(sum(Historical_Returns)/len(Historical_Returns))

End_Value = InitialInvestment * (1+averageReturn/100)**return_period

if End_Value>InitialInvestment: growth = 'increased'
elif End_Value<InitialInvestment: growth = 'decreased'
elif End_Value==InitialInvestment: growth ='stayed same'

Variance = 0

for i in Historical_Returns[:return_period+1]:
    Variance = Variance + (i-averageReturn)**2

try:
    Variance = Variance / (len(Historical_Returns) - 1)
except ZeroDivisionError:
    Variance = 0  # or any other default handling

standardDeviation = Variance**0.5

print(round(Variance,2),round(standardDeviation,2))
print(f"Your initial investment \"{growth}\" and your final value is", round(End_Value,2))
print(f'''Values based on returns are {totalReturns} 
      \n\t with Average Return (Arthemetic Mean) of {round(averageReturn,2)}''')


