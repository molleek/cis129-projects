# Module 5 Lab 5
# Mollee Kahan
# 6/22/24
# This program keeps track of how many bottles were returned in a 7 day period and the amount paid out for those bottles

#variable to track if the user wants to run the program again, data type: string
keep_going = 'y'   
#variable to hold total amount of bottles in a week, data type: int
total_bottles = 0
#variable to hold total amount of bottles in a day, data type: int
today_bottles = 0
#variable to hold total pay out in a week, data type: int
total_payout = 0
#variable to hold number of interations of for loop for 7 days, data type: int
counter = 1

#outside while loop: determines if the program runs based on user's input
while(keep_going == 'y'):
    #inside while loop: 7 iterations for each day of the week to track amount of bottles collected
    while(counter <8):
        #resets the day's bottles
        today_bottles = 0
        #gets value of today's bottles from user's entry
        today_bottles=int(input("Enter number of bottles returned for day #" + str(counter) + ": "))
        #adds today's bottles to total bottles
        total_bottles += today_bottles
        #increments counter by one to move to next day of the week
        counter += 1
    #calculates pay out based on total number of bottles
    total_payout = (total_bottles*0.10)
    #prints total number of bottles collected
    print('The total number of bottles collected is ',total_bottles)
    #prints total amount paid out
    print(f'The total paid out is $ {total_payout:.1f}')
    #resets counter, total_bottles, total_payout
    counter = 1
    total_bottles = 0
    total_payout = 0
    #prints to ask user if outer while loop should repeat
    print("Do you want to enter another week","\'","s worth of data?")
    keep_going = input('(Enter y or n): ')