
# Testing the Collatz Conjecture (3n + 1) with either a Single Seed Number (1)
# Or an interval of Seed Numbers (2)

# Importing libraries
import numpy
import math
import os

# Opening the text file that will show all the calculated data
# The file "iterationsFile.txt" must already exist for this to work
# The file path is, of course, dependent on the computer as well as the user. This path will only work for my computer/account
iterationsFile = open("iterationsFile.txt", "w")

# Function for finding the iterations of either a single seed number
# or an interval of seed numbers
def findingIterations(seedNumbersList, decision):
    iterations = 0
    iterationsList = []
    # The portion of the function that applies to a single seed number
    if (decision == 1):
        number = seedNumbersList
        while (number >= 1):
            if (number == 1):
                return iterations
            elif (math.remainder(number, 2) == 0):
                number = number/2
                iterations += 1  
            elif (math.remainder(number, 2) != 0):
                number = (3*number + 1)
                iterations += 1
    # The portion that applies to an interval of seed numbers
    elif (decision == 2):
        for number in seedNumbersList:
            # This is the code for the progress bar,
            # which is nice to have for larger intervals to keep track of execution progress
            percentagesList = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
            for percentage in percentagesList:
                if (number == (percentage*(len(seedNumbersList)))):
                    percent = (number/(len(seedNumbersList)))*100
                    print(f"{percent} %")  
            # End progress bar code
            while(number >= 1): 
                if (number == 1):
                        iterationsList.append(iterations)
                        iterations = 0
                        break
                elif ((number > 1) and (number % 2 == 0)):
                        number = number / 2
                        iterations += 1
                elif ((number > 1) and (number % 2 != 0)):
                        number = (3*number + 1)
                        iterations += 1
            return iterationsList

# Clearing the screen
os.system('cls')

# Determining whether a single seed or an interval is being tested
print("1: Single Seed Number \n2: Seed Interval")
decision = int(input("Choice: "))
if decision == 1:
    # Getting seed number
    seedNumber = int(input("Input seed number: ")) 
    # Calling function that finds the number of iterations for a given seed number
    # Setting the output of the function to the iterations  
    iterations = findingIterations(seedNumber, decision)
    # Printing output info
    print(f"Iterations: {iterations}")
elif decision == 2:
    # Getting lower and upper bounds for the interval of seed numbers
    lowerBound = int(input("Input lower bound: "))
    upperBound = int(input("Input upper bound: "))
    # Creating a list of evenly spaced integers from the lowerbound to the
    # upperbound that will be the seed numbers
    seedNumbersList = numpy.linspace(lowerBound, upperBound, (upperBound - lowerBound + 1))
    seedNumbersList = [round(number) for number in seedNumbersList]
    # Running the function for finding the interations
    iterationsList = findingIterations(seedNumbersList, decision)

    # Creating a dictionary of (key:value) = (Seed Number: Iterations)
    masterDictionary = dict(zip(seedNumbersList, iterationsList))

    # Writing the seedNumbersList, iterationsList, and masterDictionary to the iterationsFile
    iterationsFile.writelines(f"{seedNumbersList}")
    iterationsFile.writelines(f"\n{iterationsList}")
    iterationsFile.writelines(f"\nSeednumber: Iterations \n{masterDictionary}")
    # Telling user that execution is complete
    print('Done')
else:
    print("Value not compatible. Please try again.")
    
iterationsFile.close()
