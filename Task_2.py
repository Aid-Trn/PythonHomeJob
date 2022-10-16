# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

a = int(input('Enter a number in seconds '))
h = int(a // 3600) % 24
m = int(a // 60) % 60
s = a % 60
if m < 10:
    m = str('0' + str(m))
else:
    m = str(m)
if s < 10:
    s = str('0' + str(s))
else:
    s = str(s)
print(str(h) + ':' + str(m) + ':' + str(s))
