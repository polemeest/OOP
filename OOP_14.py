'''
Далее для оформления заказа нам нужен пользователь. Для этого создадим класс User, который содержит:

метод __init__, принимающий на вход логин пользователя и необязательный аргумент баланс его счета(по умолчанию 0).
Логин необходимо сохранить в атрибуте login , а баланс необходимо присвоить сеттеру   balance  (см. пункт 4)

метод __str__, возвращающий строку вида «Пользователь {login}, баланс - {balance}»
Cвойство геттер balance, которое возвращает значение self.__balance;
Свойство сеттер balance, принимает новое значение баланса и устанавливает его в атрибут self.__balance ;
метод deposit  принимает числовое значение и прибавляет его к атрибуту self.__balance ;
метод payment  принимает числовое значение, которое должно списаться с баланса пользователя.
 Если на счете у пользователя не хватает средств, то необходимо вывести фразу  «Не хватает средств на балансе.
 Пополните счет» и вернуть False. Если средств хватает, списываем с баланса у пользователя указанную сумму и возвращаем True
Пример работы с классом User

'''
'''
Последний штрих - создание класса корзины, куда наш пользователь будет складывать товары. Для этого нам понадобятся ранее созданные классы User и Product

И так, создаем класс Cart, который содержит:

метод __init__, принимающий на вход экземпляр класса User . Его необходимо сохранить в атрибуте user . 
Помимо этого метод  должен создать атрибут goods - пустой словарь (лучше использовать defaultdict). 
Он нужен будет для хранения наших товаров и их количества(ключ словаря - товар, значение - количество). 
И еще нам понадобится создать защищенный атрибут .__total со значением 0. В нем будет хранится итоговая сумма заказа
метод add принимает на вход экземпляр класса Product и необязательный аргумент количество товаров (по умолчанию 1). 
Метод add  должен увеличить в корзине (атрибут goods) количество указанного товара  на переданное значение количество и пересчитать атрибут self.__total
метод remove  принимает на вход экземпляр класса Product и необязательный аргумент количество товаров (по умолчанию 1).  
Метод remove  должен уменьшить в корзине (атрибут goods) количество указанного товара  на переданное значение количество и пересчитать атрибут self.__total.
 Обратите внимание на то, что количество товара в корзине не может стать отрицательным как и итоговая сумма
Cвойство геттер total  , которое возвращает значение self.__total;
метод order  должен использовать метод payment  из класса User и передать в него итоговую сумму корзины. 
В случае, если средств пользователю хватило, вывести сообщение «Заказ оплачен», в противном случае - «Проблема с оплатой»;
метод print_check  печатающий на экран чек. Он должен начинаться со строки
---Your check---
Затем выводится состав корзины в алфавитном порядке по названию товара в виде
{Имя товара} {Цена товара} {Количество товара} {Сумма} 
И заканчивается чек строкой
---Total: {self.total}---
'''
from collections import defaultdict

class Cart:

    def __init__(self, user):
        self.user = user
        self.goods = defaultdict(int)
        self.__total = 0

    def add(self, prod, amount = 1):
        self.goods[prod] += amount
        self.__total += prod.price * amount

    def remove(self, prod, amount = 1):
        if self.goods[prod] - amount < 0:
            self.__total -= prod.price * self.goods[prod]
            del self.goods[prod]
        else:
            self.goods[prod] -= amount
            self.__total -= prod.price * amount

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print(f'Заказ оплачен')
        else:
            print(f'Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for k in sorted(self.goods, key=lambda x: x.name):
            print(f'{k.name} {k.price} {self.goods[k]} {k.price * self.goods[k]}')
        print(f'---Total: {self.__total}---')





class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:

    def __init__(self, login, balance = 0):
        self.login = login
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.__balance}'

    def deposit(self, amount):
        self.__balance += amount

    def payment(self, amount):
        if amount > self.__balance:
            print(f'Не хватает средств на балансе. Пополните счет')
            return False
        self.__balance -= amount
        return True



billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20анс - 250