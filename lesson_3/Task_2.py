# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def personal_info(**kwargs):
    return ' '.join(kwargs.values())


print(personal_info(name=input('Enter your name: '), surname=input('Enter your surname: '),
                    birthday=input('Enter your birthday: '), city=input('Enter your city: '),
                    email=input('Enter your email: '), phone_number=input("enter your phone number: ")))

