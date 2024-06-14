"""Program descirption:
This Coffee Shop simulator calculates a customer's order and creates a 
recipt based on how many items they order."""

#creates variable coffee that store int of amt of coffee purchased
coffee = int(input("Number of coffees bought? "))
##creates variable muffin that store int of amt of muffins purchased
muffin = int(input("Number of muffins bought? "))

#creates variable coffeeCost that stores float of cost of coffee
coffeeCost = 5.00 * coffee
#creates variable muffinCost that stores float of cost of muffin
muffinCost = 4.00 * muffin

#creates variable totalNoTax: calculates total without tax
totalNoTax = coffeeCost + muffinCost

#calculates a 6% tax
tax = totalNoTax * 0.06

#creates variable total: calculates total with tax
total = totalNoTax + tax

#print recipt with correct formatting
print("\n")
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(coffee)
print("Number of muffins bought?")
print(muffin)
print("***************************************","\n")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")

#edit sentence based on how many of each item orders
if coffee == 1:
    print(coffee,"Coffee at $5 each: $", format(coffeeCost, '.2f'))
else: print(coffee,"Coffees at $5 each: $", format(coffeeCost, '.2f'))

if muffin == 1:
    print(muffin,"muffin at $4 each: $", format(muffinCost, '.2f'))
else: print(muffin,"muffins at $4 each: $", format(muffinCost, '.2f'))

print("6% tax: $", tax)
print("---------")
print("Total: $", total)
print("***************************************")