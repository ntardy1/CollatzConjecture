
# Testing the Collatz Conjecture (3n + 1) with either a Single Seed Number (1)
# Or an interval of Seed Numbers (2)

# Importing modules
import numpy
import math

# Opening the text file that will show all the calculated data
iterationsFile = open("iterationsFile.txt", "w")

# Function for finding the iterations of either a single seed number
# or an interval of seed numbers
def findingIterations(seedNumbersList, decision):
    Index = 0
    iterations = 0
    iterationsList = []
    # The portion of the function that applies to a single seed number
    if (decision == 1):
        number = seedNumbersList
        while (number >= 1):
            if (number == 1):
                iterationsList.append(iterations)
                return iterationsList
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
                    percent = (number/(len(seedNumbersList))*100)
                    print(f"{percent} %")  
            # End progress bar code
            while(number >= 1 and Index <= len(seedNumbersList) - 1):  
                if (Index > len(seedNumbersList) - 1):
                        break
                if (number == 1 and Index < len(seedNumbersList) - 1):
                        iterationsList.append(iterations)
                        iterations = 0
                        Index = Index + 1
                        number = seedNumbersList[Index]
                elif (number == 1 and Index == len(seedNumbersList) - 1):
                        iterationsList.append(iterations)
                        Index += 1
                        break
                elif ((number > 1) and (number % 2 == 0)):
                        number = number / 2
                        iterations += 1
                elif ((number > 1) and (number % 2 != 0)):
                        number = (3*number + 1)
                        iterations += 1
    return iterationsList

# Determining whether a single seed or an interval is being tested
decision = int(input("Single seed (1) or interval (2): "))
if decision == 1:
    # Getting seed number
    seedNumbersList = int(input("Input seed number: ")) 
    # Calling function that finds the number of iterations for a given seed number
    # Setting the output of the function to the iterations  
    iterationsList = findingIterations(seedNumbersList, decision)
    # Printing output info
    print(f"Seed Number: {seedNumbersList}")
    print(f"Iterations: {iterationsList}")
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
    iterationsFile.write(f"{seedNumbersList}")
    iterationsFile.write(f"\n{iterationsList}")
    iterationsFile.write(f"\nSeednumber: Iterations \n{masterDictionary}")
    # Telling user that execution is complete
    print('Done')
else:
    print("Value not compatible. Please try again.")
    
iterationsFile.close()
