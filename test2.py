sentence = input("Enter String:")
total_char = len(sentence)
num_uppercase = 0
num_lowercase = 0
num_numeric = 0
num_other = 0
for char in sentence:
    if char.isalpha():
        if char.isupper():
            num_uppercase +=1
        else:
            num_lowercase +=1
    elif char.isdigit():
        num_numeric +=1
    else:
        num_other +=1
print(f"Total alphabet = {num_uppercase + num_lowercase}")
print(f"upper_case = {num_uppercase}")
print(f"lower_case = {num_lowercase}")
print(f"Numeric = {num_numeric}")
print(f"Other letter including space = {num_other}")

    
