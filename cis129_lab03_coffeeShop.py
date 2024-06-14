"""Program descirption:
This Coffee Shop simulator calculates a customer's order and 
creates a recipt based on how many items they order. Menu 
items: coffee, muffins, iced tea, scones"""

#creates variable coffee that store int of amt of coffee purchased
coffee = int(input("Number of coffees bought? "))
##creates variable muffin that store int of amt of muffins purchased
muffin = int(input("Number of muffins bought? "))
#creates variable icedTea that store int of amt of iced tea purchased
icedTea = int(input("Number of iced teas bought? "))
##creates variable scone that store int of amt of scones purchased
scone = int(input("Number of scones bought? "))

#creates variable coffeeCost that stores float of cost of coffee
coffeeCost = 5.00 * coffee
#creates variable muffinCost that stores float of cost of muffin
muffinCost = 4.00 * muffin
#creates variable icedTeaCost that stores float of cost of iced tea
icedTeaCost = 3.00 * icedTea
#creates variable sconeCost that stores float of cost of cost
sconeCost = 2.00 * scone

#creates variable totalNoTax: calculates total without tax
totalNoTax = coffeeCost + muffinCost + icedTeaCost + sconeCost

#calculates a 6% tax
tax = totalNoTax * 0.06

#creates variable total: calculates total with tax
total = totalNoTax + tax

#print recipt with correct formatting
print("\n")
print("***************************************")
print("Carla's Coffee Shop")
print("Number of coffees bought?")
print(coffee)
print("Number of muffins bought?")
print(muffin)
print("Number of iced teas bought?")
print(icedTea)
print("Number of scones bought?")
print(scone)
print("***************************************","\n")
print("***************************************")
print("Carla's Coffee Shop Receipt")

#edit sentence based on how many of each item orders
if coffee == 1:
    print(coffee,"Coffee at $5 each: $", format(coffeeCost, '.2f'))
else: print(coffee,"Coffees at $5 each: $", format(coffeeCost, '.2f'))

if muffin == 1:
    print(muffin,"Muffin at $4 each: $", format(muffinCost, '.2f'))
else: print(muffin,"Muffins at $4 each: $", format(muffinCost, '.2f'))

if icedTea == 1:
    print(icedTea,"Iced tea at $3 each: $", format(icedTeaCost, '.2f'))
else: print(icedTea,"Iced teas at $3 each: $", format(icedTeaCost, '.2f'))

if scone == 1:
    print(scone,"Scone at $2 each: $", format(sconeCost, '.2f'))
else: print(scone,"Scones at $2 each: $", format(sconeCost, '.2f'))

print("6% tax: $", tax)
print("---------")
print("Total: $", total)
print("***************************************")

print("Thank you for coming to Carla's Coffee Shop!")
