file = open("declaration.txt","r")

wordDict = {}
#print(file.read())

data = file.readlines()
wordCopy = ""

for line in data:
    for word in line.split():
        #checking to see if the word has any smybols other than a letter
        for letter in word:
            if letter >= 'a' and letter <= 'z' or letter >= 'A' and letter <= 'Z':
                wordCopy += letter
            wordCopy = wordCopy.lower();
        #print(wordCopy)
        if(wordCopy not in wordDict):
            wordDict[wordCopy] = 1
        else:
            wordDict[wordCopy] += 1
        wordCopy = ""
        
    #print(word)

#wordDict = sorted(wordDict)

print(wordDict['in'])

#print(words)
