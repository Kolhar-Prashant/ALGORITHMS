# Euclid's Algorithm to find GCD.
def calc_GCD(divisor,dividend):
    rem = -1
    while (rem != 0):
        rem = dividend % divisor
        dividend = divisor
        divisor = rem
    return dividend

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
GCD=0
GCD=calc_GCD(a,b)
print("Greatest common divisors of", a, b, "is", GCD)
