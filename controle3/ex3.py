from math import exp

x = [i for i in range(-5,6)]
y1 = [i**2 for i in x]
y2 = [exp(i) for i in x]

print(str(x))
print(str(y1))
print(str(y2))

from matplotlib.pyplot import plot, show
plot(x, y1)
plot(x, y2)
show()
