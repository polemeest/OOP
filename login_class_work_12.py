'''
Допустим, у нас есть сайт и для успешной регистрации на нем необходимо придумать логин и пароль. Но мы хотим,
чтобы при этом выполнялись определенные проверки с предоставленной пользователем информацией, например, чтобы пароль был непростым.
Мы можем делегировать данные проверки классу Registration , который вам необходимо создать.

Задача будет состоять из двух частей.

Часть 1
Создайте класс Registration, который пока будет проверять только введенный логин. Под логином мы будем
подразумевать почту пользователя, поэтому необходимо будет сделать некоторые проверки.

В классе Registration необходимо реализовать:

метод __init__ принимающий один аргумент логин пользователя. Метод __init__ должен сохранить переданный логин
через сеттер (см пункт 3). То есть когда отработает данный код

def __init__(self, логин):
    self.login = логин # передаем в сеттер login значение логин
должно сработать свойство сеттер login из пункта 3 для проверки валидности переданного значения

Cвойство геттер login, которое возвращает значение self.__login;
Свойство сеттер login, принимает значение нового логина. Новое значение мы должны проверить на следующее:
логин, так как является почтой, должен содержать один символ собаки «@». В случае, если в логине отсутствует символ «@»,
 вызываем исключение при помощи строки raise ValueError("Логин должен содержать один символ '@'")
логин должен содержать символ точки «.» после символа «@».В случае, если после @ нету точки, вызываем исключение при
помощи строки raise ValueError("Логин должен содержать символ '.'")
Если значение проходит проверку новое значение логина сохраняется в атрибут self.__login

if error:
    raise ValueError("Login must include at least one ' @ '")
'''
from string import ascii_letters

class Registration:

    @staticmethod
    def is_include_all_register(password):
        key = set([1 for i in password if i.isalpha() == True and i == i.lower()]) | set([2 for i in password if i.isalpha() == True and i == i.upper()])
        return key

    @staticmethod
    def is_include_only_latin(password):
        for i in password:
            if i.isalpha() == True and i not in ascii_letters:
                return False
        return True

    @staticmethod
    def check_password_dictionary(password):
        if password not in open(r'easy_passwords.txt').read().strip():
            return True
        return False

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        elif len(password) < 4 or len(password) > 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        elif len([i for i in password if i.isdigit() == True]) < 1:
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif len(Registration.is_include_all_register(password)) != 2:
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        elif Registration.is_include_only_latin(password) == False:
            raise ValueError('Пароль должен содержать только латинский алфавит')
        elif Registration.check_password_dictionary(password) == False:
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = password



    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if "@" not in login:
            raise ValueError("Login must include at least one ' @ '")
        if '.' not in login or login.index('.') < login.index('@'):
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = login

#
# if value.count('@') != 1: raise ValueError("Логин должен содержать один символ '@'")
#         if '.' not in value[value.find('@'):]: raise ValueError("Логин должен содержать символ '.'")
#         self.__login = value

r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
#r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
#r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#r1.password = 43  # raise TypeError("Пароль должен быть строкой")








