#! /usr/bin/env python3

import sys        # command line argument

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()
        
outputFname = sys.argv[2]
inputFname = sys.argv[1]

file = open(inputFname,"r")
wordDict = {}

data = file.readlines()
wordCopy = ""

# Checks to see if symbol is a valid letter
def letterCheck(str):
    if letter >= 'a' and letter <= 'z' or letter >= 'A' and letter <= 'Z':
        return 1
    return 0

# Checks to see if word is in the dictionary
def dictionaryCheck(str):
    if wordCopy not in wordDict:
        return 1
    return 0

# Loop first reads line of data then a specific word in a line then the letter of a specific word
for line in data:
    for word in line:
        for letter in word:
            if letterCheck(letter) == 1:
                wordCopy += letter
            else:
                wordCopy = wordCopy.lower()
                if dictionaryCheck(wordCopy) == 1:
                    wordDict[wordCopy] = 1

                else:
                    wordDict[wordCopy] += 1
                wordCopy = "" # Clears word copy so a new word can be copied
                
del(wordDict['']) # deletes number of spaces counted from dictionary
keys = wordDict.items() # Setting keys equal to all the items in the dictionary
wordDict = sorted(keys) # Sorts items in dictionary

count = 1 # Count is simply used so the data in file is properly formatted

outputFile = open(outputFname,"w") # opens output file

for k in wordDict:
    for i in k:
        if count is 1:
            outputFile.write(str(i))
            count = count + 1
        elif count is 2:
            outputFile.write(" "+str(i)+"\n")
            count = 1
        
outputFile.close() # closes output file
