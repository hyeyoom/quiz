a = 1
b = 2
c = 0

while b <= 4000000:
    if b % 2 is 0:
        c += b
    a, b = b, a + b

print c
