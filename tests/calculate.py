import time

x = 1
for i in range(20, 39):
    x *= i
y = 1
for i in range(1, 20):
    y *= i
print(x / y)