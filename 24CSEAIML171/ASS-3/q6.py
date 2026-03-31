#wap to remove all duplicate alphabets from a given string
x=input("Enter a string:")
result=""
for char in x:
    if char not in result:
        result=result+char
print(result)