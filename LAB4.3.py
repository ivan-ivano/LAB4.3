# < Іваньо Іван >
# Лабораторна робота № 4.3
# Табуляція функції, заданої формулою: функція з параметрами.
# Варіант 0.6

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

X_start = int(input("X_поч: "))
X_end = int(input("X_кін: "))
dX = int(input("dX: "))

print('---------------------------')
print('|   X   |   F   |')
print('---------------------------')

x = X_start

while x <= X_end:
    if c < 0 and b != 0:
        F = a * (x ** 2) + (b ** 2) * x
    elif c > 0 and b == 0:
        F = (x + a) / (x + c)
    else:
        F = x / c

    print('|   '+str(x)+'   |   '+str(round(F, 3))+'   |')

    x += dX

print('---------------------------')
