a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
gcd = 1
i = 1
while i <= a and i <= b and i <= c:
    if a % i == 0 and b % i == 0 and c % i == 0:
        gcd = i
    i += 1
print("GCD of the three numbers is:", gcd)
