def sum_oflist(l1):
    return sum(l1)
n=int(input(" enter noof elements"))
l1=[]
for i in range(n):
    l1.append(int(input(f"enter  elements")))
    print("sum of elements",sum_oflist(l1))