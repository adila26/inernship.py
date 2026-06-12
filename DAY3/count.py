sentence=input("enter a sentence:")
frequency={}
for word in sentence.split():
    frequency[word]=frequency.get(word,0)+1
print(frequency)    