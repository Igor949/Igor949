class House():
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
            if(new_floor > self.number_of_floors  or  new_floor < 1):
                print("Такого этажа не существует")
            else:
                 for i in range (int(new_floor)):
                     print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.__eq__(other) or self.__lt__(other)


    def __gt__(self,other):
        return not self.__le__(other)

    def __ge__(self,other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)


    def __add__(self, value):  # h1 = h1 + 10 или h1 = h1 + h2
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other: int):
        return self.__add__(other)



h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 12)
h1.go_to(10)
h2.go_to(2)
# __len__
print(len(h1))
print(len(h2))
# __str__
print(h1)
print(h2)
# __eq__
print(h1 == h2, "__eq__")
# __lt__
print(h1 < h2, "__lt__")
# __le__
print(h1 <= h2, "__le__")
# __gt__
print(h1 > h2, "__gt__")
# __ge__
print(h1 >= h2, "__ge__")
# __ne__
print(h1 != h2, "__ne__")
# __add__
h1 = h1 + 10
print(h1, "__add__")
print(h1 == h2,"__add__")
#__rad__
h1 = h1 + 5
print(h1,"__rad__")
print(h1 == h2, "__rad__")
#_iadd__
h1 = h1 + 1
print(h1, "__iadd")
print(h1 != h2, "__iadd__")
