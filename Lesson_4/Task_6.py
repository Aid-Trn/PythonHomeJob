# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count, cycle

my_count = count(7)
my_cycle = cycle('ABC')

for _ in range(5):
    print('(my_count, my_cycle) = ({},{})'.format(next(my_count), next(my_cycle)))
