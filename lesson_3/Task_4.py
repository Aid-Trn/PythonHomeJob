# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return 'Enter a float number and negative power'
    return res


print(my_pow_fun(3.6, -4))
