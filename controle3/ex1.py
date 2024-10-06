
x = int(input("x="))
y = int(input("y="))

reste = x % y
while reste != 0:
    x = y
    y = reste
    reste = x % y
print("pgcd =", y)
