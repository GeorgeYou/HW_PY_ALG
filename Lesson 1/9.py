# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# https://drive.google.com/file/d/1FFpighQdEcX7Uet27TfpJJ7nPwOLcxau/view?usp=sharing

a = float(input('Введите число а: '))
b = float(input('Введите число b: '))
c = float(input('Введите число c: '))

if b > a > c or b < a < c:
    print(a)
elif a < b < c or a > b > c:
    print(b)
else:
    print(c)
