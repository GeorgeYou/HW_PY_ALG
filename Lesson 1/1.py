# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1r7oMTCV1lIpiDVVe9Ucv-1ot8vVZbkX8/view?usp=sharing

a = int(input('Введите трехзначное число: '))

b = a % 10
c = a // 10 % 10
d = a // 100
e = b + c + d
f = b * c * d

print(e)   # сумма
print(f)   # произведение