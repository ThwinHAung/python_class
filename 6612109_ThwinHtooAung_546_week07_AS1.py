input_words =input("Enter words: ").split()
count=0
for i in input_words:
if len(i)>4 and i[0]==i[-1]:
count+=1
print("Number of words that meets the
requirements is: ",count)
