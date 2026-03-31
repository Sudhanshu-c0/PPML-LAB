def count_vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text:
        if char in vowels:
            count += 1
    return count
s=input("Enter a string:")
result=count_vowels(s)
print("Number of vowels in the String is:",result)