words = []

keys = str(input('Enter Words: \n'))

if keys.isalpha():
    print("Here is the results: ")
else:
    print("That's not a word dummy!")
user_words = keys.split()
#[item.lower() for item in user_words]
words.append(keys.lower())
for i in words:
    j = i.replace(' ','')
#print("".join(words))
print(j)
