class City:

    def __init__(self, city_name):
        self.name = str(city_name).title()

    def __str__(self):
        return self.name

    def __bool__(self):
        lst = ('a', 'e', 'i', 'o', 'u')
        return self.name[-1] not in lst


p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"