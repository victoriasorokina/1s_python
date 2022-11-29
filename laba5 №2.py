import random
import matplotlib.pyplot
import numpy
import math
n = int(input("Введите количество символов:"))
a = []
for i in range (n):
    a1 = random.randint(0, 100)
    a.append(a1)
print (a)
m = sum(a)/n
print ("Математическое ожидание:", m)
otkl = math.sqrt(sum(((i - m)**2 for i in a))/n)
print ("Среднеквадратичное отклонение:", otkl)
k = random.randint (0,100)
b = random.randint (0,100)
f = numpy.array([k*i+b for i in range (n)])
y = f+numpy.random.normal(m, otkl, n)
x = numpy.array(range (n))
mx = sum(x)/n
my = sum(y)/n
ax = numpy.dot(x.T, x)/n
ay = numpy.dot(x.T, y)/n
k1 =(ay-mx*my)/(ax-mx**2)
b1 = my-k1*mx
f1 = numpy.array([k1*i+b1 for i in range (n)])
matplotlib.pyplot.plot(f)
matplotlib.pyplot.plot(f1)
matplotlib.pyplot.scatter(x, y)
matplotlib.pyplot.grid()
matplotlib.pyplot.show()