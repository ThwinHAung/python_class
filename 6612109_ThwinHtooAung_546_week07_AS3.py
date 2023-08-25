Char=input("Input: ").split()
n=int(input("Enter a value for n: "))
output=[]
for char in Char:
  for i in range(1,n+1):
    string=char.upper()+str(i)
    output. append(string)
print("Output:",''.join(output))
