# 5. Запросите у пользователя значения выручки и издержек фирмы.

revenue = int(input('Enter the amount of revenue: '))
costs = int(input('Enter the amount of costs: '))

if revenue > costs:
    print(f'The company operates with profit in {revenue / costs:.2f}')
    staff = int(input('Specify the number of employees '))
    print(f'The company profit per employee = {revenue / staff:.2f}')

elif revenue == costs:
    print('The amount of costs is equal to income! ')

else:
    print('The amount of costs exceeds the income! ')
