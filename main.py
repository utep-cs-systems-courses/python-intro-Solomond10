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
        #wordDict = sorted(wordDict,key = wordCopy)
        if(wordCopy not in wordDict):
            wordDict[wordCopy] = 1
        else:
            wordDict[wordCopy] += 1
        wordCopy = ""
        
keys = wordDict.items()
wordDict = sorted(keys)
#print(wordDict[0])


count = 0

outputFile = open("output.txt","w")
for k in wordDict:
    #print("INSIDE LOOP: ", k)
    #a = k.split(",")

    #print("INSIDE LOOP: ", k)
    #outputFile.write(str(k)+"\n")

    for i in k:
        if count is 0:
    #print("INSIDE INSIDE LOOP: ", i)
            outputFile.write(str(i))
            count = count + 1
        elif count is 1:
            outputFile.write(" "+str(i)+"\n")
            count = 0
        
outputFile.close()

