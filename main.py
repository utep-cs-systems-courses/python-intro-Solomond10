print("Hello World")

file = open("declaration.txt","r")

wordDict = {}
#print(file.read())

data = file.readlines()

for line in data:
    for word in line.split():
        for letter in word:
            if letter <= 'a' and >= 'z' or <= 'A' and >= 'Z':
                print(letter)
        #if(word not in wordDict):
         #   wordDict[len(wordDict)] = (word,1)
    #print(word)

#print(wordDict)
#words = { 'word': 'When', 'count': 1, }

#print(words)
