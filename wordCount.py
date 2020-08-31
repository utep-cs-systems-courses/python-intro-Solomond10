#! /usr/bin/env python3

import sys        # command line argument
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()
        
outputFname = sys.argv[2]
inputFname = sys.argv[1]

#file = open("declaration.txt","r")
file = open(inputFname,"r")
wordDict = {}
#print(file.read())

data = file.readlines()
wordCopy = ""

#print("word dictionary: ", wordDict)
for line in data:
    #print(line)
    #for word in line:
    for word in line.split():
        #checking to see if the word has any smybols other than a letter
        #print(word)
        for letter in word:
            #print(word)
            if letter >= 'a' and letter <= 'z' or letter >= 'A' and letter <= 'Z':
                wordCopy += letter
           # elif letter == '-':
            #    continue
            else:
                break
            #    print(letter)
             #   wordCopy = ""
            wordCopy = wordCopy.lower();
        if(wordCopy not in wordDict):
            wordDict[wordCopy] = 1
        else:
            wordDict[wordCopy] += 1
        wordCopy = ""
        
keys = wordDict.items()
wordDict = sorted(keys)

count = 0

outputFile = open(outputFname,"w")
for k in wordDict:
    for i in k:
        if count is 0:
            outputFile.write(str(i))
            count = count + 1
        elif count is 1:
            outputFile.write(" "+str(i)+"\n")
            count = 0
        
outputFile.close()
