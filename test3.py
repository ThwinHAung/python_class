#split string
sentence = input("Write a sentence:")
length = len(sentence)
print(sentence[0:length//2])
print(sentence[length//2:length])
#reverse string
myStr = "Hello This is from Thailand"
revMyStr = myStr[::-1]
print(revMyStr)

#replace string
orgStr = 'banana,banana milkshake,banana smoothie,banana soda'
repStr = orgStr.replace('banana','strawberry')
print(orgStr)
print(repStr)

