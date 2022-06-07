
# Creating visualizations of the data obtained from
# the FindingIterations program

# Importing modules
import numpy
import math
import matplotlib.pyplot as plt

# Importing data from FindingIterations program
# and related text file(s)
rawData = open(r"C:\Users\laten\Desktop\Projects\Python\CollatzConjecture\iterationsFile.txt", "r")
dataset = rawData.readlines()
rawSeedNumbers = dataset[0]
rawIterations = dataset[1]
rawMaxNumbers = dataset[2]
rawData.close()

rawSeedNumbers = rawSeedNumbers.replace("[", "")
rawSeedNumbers = rawSeedNumbers.replace("]", "")
rawSeedNumbers = rawSeedNumbers.replace("\n", "")
newSeedNumbers = rawSeedNumbers.split(", ")

rawIterations = rawIterations.replace("[", "")
rawIterations = rawIterations.replace("]", "")
rawIterations = rawIterations.replace("\n", "")
newIterations = rawIterations.split(", ")

rawMaxNumbers = rawMaxNumbers.replace("[", "")
rawMaxNumbers = rawMaxNumbers.replace("]", "")
rawMaxNumbers = rawMaxNumbers.replace("\n", "")
rawMaxNumbers = rawMaxNumbers.replace(", ")

percentagesList = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

lowerBound = int(input("Lower bound (Min = 0): "))
upperBound = int(input(f"Upper bound (Max = {len(newIterations)}): "))

newSeedNumbers = rawSeedNumbers
newIterations = rawIterations
newMaxNumbers = rawMaxNumbers
lowerIndex = newSeedNumbers.index(str(lowerBound))
upperIndex = newSeedNumbers.index(str(upperBound))

newSeedNumbers = newSeedNumbers[lowerIndex:upperIndex + 1]
newIterations = newIterations[lowerIndex:upperIndex + 1]
newMaxNumbers = newMaxNumbers

'''
for k in range(0, upperBound - lowerBound + 2):
    newSeedNumbers[k] = int(newSeedNumbers[k + lowerBound])
    newIterations[k] = int(newIterations[k + lowerBound])

for i in range(lowerBound, upperBound):
    newIterations[i] = int(newIterations[i])
    newSeedNumbers[i] = int(newSeedNumbers[i])
    for percent in percentagesList:
        if (i == percent*len(newIterations)):
            print(f"{i/len(newIterations) * 100} %")

plt.scatter(newSeedNumbers, newIterations)
for j in range(0,len(newIterations)):
    plt.annotate((f"{newSeedNumbers[j]}, {newIterations[j]}"), (newSeedNumbers[j], newIterations[j]))
plt.show()
'''
labels = input("Labels (y or n): ")
plt.scatter(newSeedNumbers, newIterations)
if (labels == 'y'):
  for j in range(0,len(newSeedNumbers)):
      plt.annotate((f"{newSeedNumbers[j]}, {newIterations[j]}"), (newSeedNumbers[j], newIterations[j]))
plt.title("Iterations")
plt.show()

plt.scatter(newSeedNumbers, maxNumbers)
if (labels == 'y'):
  for j in range(0,len(newSeedNumbers)):
      plt.annotate((f"{newSeedNumbers[j]}, {maxNumbers[j]}"), (seedNumbersList[j], maxNumbers[j]))
plt.title("Maximums")
plt.show()
