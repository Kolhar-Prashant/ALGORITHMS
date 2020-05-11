
def calc_GCD(divisor,dividend):
    quo = 0
    rem = -1
    while (rem != 0):
        quo = dividend // divisor
        rem = dividend % divisor
        dividend = divisor
        divisor = rem
    return dividend

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
GCF=0
GCF=calc_GCD(a,b)
print("Greatest common divisors of", a, b, "is", GCF)