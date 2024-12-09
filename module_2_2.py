n1 = int(input('input 1st number:'))
n2 = int(input('input 2nd number:'))
n3 = int(input('input 3rd number:'))

if n1 == n2 and n1 == n3:
    print(3)
elif n1 == n2 or n1 == n3 or n2 == n3:
    print(2)
else:
    print(0)