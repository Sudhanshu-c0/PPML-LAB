list = []
n = int(input("Enter number of elements: "))
for i in range(n):
    list.append(int(input()))
list = list(set(list))  
list.sort()        
print("Sorted list without duplicates:", lst)
