# abelian.py
# Max Liang
# created 04/18/23
# Description:
#
#


def generate_primes(n):
    primes = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes


def abelian(n):
    prime_list = generate_primes(n)
    if n not in prime_list:
        factor_list = []
        N = n
        while N != 1:
            for i in prime_list:
                if N % i == 0:
                    factor_list.append(i)
                    N = int(N / i)
                    break
        return factor_list
    else:
        return [n]



