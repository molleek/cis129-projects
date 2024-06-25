# Module 6 Lab 6
# Mollee Kahan
# 6/24/24
# This program detrmines the number of packages of hot dog/buns and the number of hot dogs/buns 
# leftover for a cookout. The output is based on the maximum number of attendees and the amount
# of hot dogs designated to each attendee. This program assumes that 10 hot dogs come in a pack
# and 8 hot dog buns come in a pack.

def getTotalHotDogs():
    """This function determines how many hot dogs are needed for the cookout based on the user's inputs"""

    #local variable for the number of attendees, data type: int
    attendees = int(input('What is the maximum number of attendees for your cookout? '))
    #local variable for the number of hot dogs per each attendee, data type: int
    hotDogs = int(input('How many hot dogs do you want to designate to each attendee? '))
    
    #local variable for the total number of hot dogs, data type: int
    total = attendees * hotDogs
    
    #returns total as an int
    return total

def showResults(total):
    """this function determines and prints the amount of hot dogs/buns left over and the minimum amount of hot dogs/buns 
    packages needed for the cookout. It requries one parameter, total, which is an int for the amount of hot dogs 
    required for the cookout."""
    
    #constant for the amount of hot dogs in a package
    DOGS = 10
    #constant for the amount of hot dog buns in a package
    BUNS = 8

    #calculations for number of hot dogs/buns left, data type: int
    dogsLeft = ((DOGS - (total%DOGS))%DOGS)
    bunsLeft = ((BUNS - (total%BUNS))%BUNS)

    #calculations for number of minimum number of hot dog/bun packages needed, data type: int
    minDogs = int((total / DOGS) + (0 ** (0 ** dogsLeft)))
    minBuns = int((total / BUNS) + (0 ** (0 ** bunsLeft)))

    #print statements for hot dog/bun packages and leftovers
    print('Minimum packages of hot dogs needed:',minDogs)
    print('Minimum packages of hot dog buns needed:',minBuns)
    print('Hot dogs remaining:',dogsLeft)
    print('Hot dog buns remaining:',bunsLeft)

#call to totalHotDogs function
totalHotDogs = getTotalHotDogs()
#call to showResults using totalHotDogs as parameter
showResults(totalHotDogs)
