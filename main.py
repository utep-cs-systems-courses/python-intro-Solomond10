print("Hello World")

file = open("declaration.txt","r")

wordDict = {'word': 'value'}
#print(file.read())

data = file.readlines()
wordCopy = ""

for line in data:
    for word in line.split():
        #checking to see if the word has any smybols other than a letter
        for letter in word:
            if letter >= 'a' and letter <= 'z' or letter >= 'A' and letter <= 'Z':
                wordCopy += letter
        #print(wordCopy)
        if(wordCopy not in wordDict):
            wordDict[len(wordDict)] = (wordCopy,1)
        else:
             wordDict[wordCopy] = value + 1
        wordCopy = ""
        
    #print(word)

#print(wordDict[1])
print(wordDict)
#words = { 'word': 'When', 'count': 1, }

#print(words)
