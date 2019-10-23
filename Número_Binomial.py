n = int(input("Digite N:"))
k = int(input("Digite K:"))
binomio = 0

def fatorial (x):
    y = x
    i = 1
    while y >= 1 :
        i = y * i
        y = y - 1
    return i

binomio = fatorial (n) / (fatorial(k) * fatorial(n-k))

print("O número binomial de N/K é:",binomio)


