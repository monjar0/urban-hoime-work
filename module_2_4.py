#Primes: [2, 3, 5, 7, 11, 13] - делятся на 1 и само себя кроме 1
#Not Primes: [4, 6, 8, 9, 10, 12, 14, 15] - все остальные кроме 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


for k in numbers:
    if k == 1:
        continue

    is_prime = True
    for i in range(2, k):
        if k % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(k)
    else:
        not_primes.append(k)
print('primes:', primes)
print('not primes:', not_primes)