# Module 11, Lab 11: 9.1
# Mollee Kahan
# 7/19/24
#This program will store any amount of grades into a text file called "grades.txt"

#using the with keyword and w mode to signify writing to "grades.txt"
with open('grades.txt', mode='w') as grades:
    #variable to keep track if user wants to continue to add grades
    userInput = 1
    
    #while loop to allow the user to input as many grades as they want
    while userInput != -1:
        userInput = int(input('Enter a grade or type -1 to quit: '))
        #writes user's input to the txt file
        if userInput != -1:
            print(userInput,file=grades)        

# Module 11, Lab 11: 9.2
# Mollee Kahan
# 7/19/24
#This program will read "grades.txt" and display the individual grades, total of the 
# grades (total), number of grades entered (count), and the average of the grades

#using the with keyword and r mode to signify reading from "grades.txt"
with open('grades.txt', mode = 'r') as grades:
    #creates a list of strings with each grade
    numList = grades.read().splitlines()
    
    #variables to hold total, count, and average
    total = 0
    count = 0
    average = 0
    
    #for loop to covert each string to a float and to find the sum of the list
    for number in numList:
        total += float(number)
    
    #calculating the total number of grades in the list
    count = len(numList)
    #calculating the average
    average = total/count

    #printing grades, total, count, and average
    print("Grades:",numList)
    print("Total:",total)
    print("Count:",count)
    print("Average:",average)

# Module 11, Lab 11: 9.3
# Mollee Kahan
# 7/19/24
#This program will store a csv file called "grades.csv" that will hold a student's 
# first/last name and last 3 exam grades in the format: firstname,lastname,exam1grade,exam2grade,exam3grade

#importing csv module
import csv

#using the with keyword and w mode to signify writing to "grades.csv"
with open('grades.csv', mode='w', newline='') as grades:
    #variable to keep track if user wants to continue to add students
    keepGoing = 1
    #creates writer object that writes to grades
    writer = csv.writer(grades)
    #while loop to allow the user to input as many students as they want
    while keepGoing != -1:
        userFirstName = input("Enter student's first name or type -1 to quit: ")
        if userFirstName != "-1":
            userLastName = input("Enter student's last name: ") 
            userExam1 = int(input("Enter student's exam 1 grade: "))
            userExam2 = int(input("Enter student's exam 2 grade: "))
            userExam3 = int(input("Enter student's exam 3 grade: "))
            #writing to the csv file in correct format
            writer.writerow([userFirstName,userLastName,userExam1, userExam2,userExam3])
        else:
            #stops the while loop by changing keepGoing
            keepGoing = -1