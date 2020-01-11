import numpy as np
import matplotlib.pyplot as plt

p=0
q=0
err=0
newX=0
newY=0
population=[]
profit=[]
fin=open('ex1data1.txt')
for line in fin:
    pointer = line.split(",")
    population.append(float(pointer[0]))
    profit.append(float(pointer[1]))
m=len(population)
for x,y in zip(population,profit):
        assumption=p+(q*x)
        error=(assumption-y)**2
        err=err+error
err=err/(2*m)
earlier=err
def cal1(u,v):
    sum = 0
    m = len(population)
    for x, y in zip(population,profit):
        assumption = u+(v*x)
        error = (assumption-y)
        sum = sum+error
    sum = 0.01*(sum/m)
    newX=u-sum
    return newX
def cal2(u,v):
    sum = 0
    m = len(population)
    for x, y in zip(population,profit):
        assumption= u + (v * x)
        error = (assumption - y)*x
        sum = sum + error
    sum = 0.01*(sum /m)
    newY=v-sum
    return newY
newTheetaX=cal1(p,q)
newTheetaY=cal2(p,q)
p=newTheetaX
q=newTheetaY
err = 0
m = len(population)
for x, y in zip(population, profit):
    assumption = p + (q * x)
    error = (assumption - y)**2
    err = err + error
err = err/(2*m)
now=err
while(earlier>now):
    newTheetaX=cal1(p,q)
    newTheetaY=cal2(p,q)
    p=newTheetaX
    q=newTheetaY
    earlier=now
    err = 0
    m = len(population)
    for x, y in zip(population, profit):
        assumption = p + (q * x)
        error = (assumption-y)**2
        err = err + error
    err = err / (2 * m)
    now = err
plt.title("Bakery Franchise Plot")
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
plt.yticks([-5, 0, 5, 10, 15, 20, 25])
plt.xlabel("Population of City in 10,000s")
plt.ylabel("Profit in $10,000s")
plt.scatter(population,profit,label="Training Data",marker="x",color="red")
axes = plt.gca()
xMark = np.array(axes.get_xlim())
yMark = p + q * xMark
plt.plot(xMark,yMark,'-',label="Regression Line",lw=2,color="black")
plt.legend(loc=4)
plt.show()