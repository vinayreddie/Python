import numpy as np   ##syntax to import any libraries
PV=10000   ## declaring integer & one way of declaring variable. ex a=10, b=20, c=30
r,n=7.00/100,5.00 ## float & other way of declaring variables. ex a.b,c = 10,20,30
single,doublequote='peter',"john" ## a string can be declared in both single and double quotes
FV = PV * (1+r)**n  ##** represent exponential value ^
## Declaring array using List
## Way 1
Inflation_Historical = [3,4,6.4,7.7,7.5]
Debt = (200,300,150,400,97)  ## represented in million. multiply with 1e6 for actual value
 ##tupples --no modification can be done

Company_A_Fundamentals = {
                           'Market_Cap': 250,
                           'Share_Price' : 148.34,
                           'outstanding_shares' : (250 * 1e6)/ 148.34
}
## Syntax to create a dictionary
## Alternatively we can use () brackets to create a dictionary and we dont need quotes 
## company_fundamentals = dict(market_cap = 251, share_price = 148.34)
print(Company_A_Fundamentals)

Week_Low_52 = 142.96
Week_High_52 = 156.78
##adding new elements to dictionary
Company_A_Fundamentals['52_Week_Low'] = Week_Low_52
Company_A_Fundamentals['52 Week High'] = Week_High_52
print(Company_A_Fundamentals)
## Print individual items in dictionary
print(Company_A_Fundamentals['Share_Price'])
Company_A_Fundamentals['Market_Cap']=251 ##updating a value in dictionary
print(Company_A_Fundamentals)
##syntax to delete an item from dictionary ---- del dictionaryname[key]
## For Lists , indexing always start from 0
## there are 2 indexes for each element in the array
## negative indexing, positive indexing
##slice notion defaults
##[ :4] --gives list till 4th index, [1: ] --- starts from 1st index
slice_to = Inflation_Historical[:2]
slice_from=Inflation_Historical[2:]
print(slice_to,slice_from)


Positive_Index = Inflation_Historical[4]  # starts with 0 from left to right
Negative_Index = Inflation_Historical[-1] # starts with -1 from Right to left
##Why -ve indexing: When we don't know actual length of array and want to get
## a value from list. 
print("PI :",Positive_Index, "NI :",Negative_Index)
print(Inflation_Historical[len(Inflation_Historical)-1]) #Get last element in the array
print("slicing",Inflation_Historical[-3:])

##stepper in list
## gives sublist of every nth number [index start:index end:n] n is stepper
stepper_inflation = Inflation_Historical[1:5:2] # gives every second number
print("stepper inflation:",stepper_inflation)
##modify values in array

Inflation_Historical[0] = 3.4

print("corrected: " ,Inflation_Historical)

## Way 2
stock_price = []  ##This create empty list at first
##to insert elements into empty list we can use append(),
#  extend(),insert(index, value), concatenate, generate values dynamically, repeat elements
historical_returns = np.array([7.00,8.00,10.00,13.56,14.00])
##lets use append to insert initial value
stock_price.append(252.56) 
##print(stock_price)

##lets calculate final stock price based on historical returns
## FV = PV (1+r)^n --- Base Formula

np.set_printoptions(legacy='1.25')
new_price = stock_price[0]
for i in historical_returns[:5]: 
    new_price=new_price*(1+i/100) 

    stock_price.append(round(new_price,2))


print("Stock Price based on the returns: ",stock_price)


## Get a range of values from an array using indexes
## list[Start:end] --- end represents index where slicing stops. this do not include actual value of end index

Range_Inflation = Inflation_Historical[1:4]
print(Range_Inflation)  ## Only prints [4, 6.4, 7.7]. 

#declaring array using numpy library

historical_decimal = historical_returns / 100  # Convert percentages to decimals
##values_to_use = historical[:50] / 100

##arthemetic_mean = np.mean(historical) #With np.mean

arthemetic_mean = sum(historical_returns)/len(historical_returns)
##To round the value to nearest whole number while dividing
#arthemetic_mean = sum(historical)//len(historical)
#  : used // to round to whole number --- Floor Divison
##geometric_mean1 = (np.prod(1+historical)**(1/n))-1 ##with function

product = 1
for i in historical_returns[:5]: product*=(1 + i)

geometric_mean = product**(1/len(historical_returns))-1

print ("Future value with",PV, r,n ,"is", round(FV,2))

print("Arthemetic Mean : ".upper(),int(round(arthemetic_mean,2)))

print('Geometric Mean : '.lower(),round(geometric_mean,2))
# %s represents string, %d represents int, %f represents float
message = 'the am is %f, gm is %.2f' %(arthemetic_mean,geometric_mean)
## we can either take formatting into variable or we can directly 
## use in print statement.
print('the am is %f, gm is %.2f' %(arthemetic_mean,geometric_mean))