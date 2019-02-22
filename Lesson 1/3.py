# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

# https://drive.google.com/file/d/1JgGHfeL791LxdONyUYgF-u-YaJx6TF2p/view?usp=sharing

x1 = float(input('Введите координату х1: '))
y1 = float(input('Введите координату y1: '))
x2 = float(input('Введите координату x2: '))
y2 = float(input('Введите координату y2: '))

if x1 != x2:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print('y=', k, 'x +', b)
else:
    print('x=', x1)
