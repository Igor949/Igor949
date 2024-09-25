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
        return self.name == other

    def __lt__(self,other):
        return self.name < other.name

    def __le__(self,other):
        return self.name <= other.name

    def __gt__(self,other):
        return self.name > other.name

    def __ge__(self,other):
        return self.name >= other.name


    def __add__(self, value):
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.number_of_floors + value

    def __iadd__(self,value):
        return self.number_of_floors + value



h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
h1.go_to(25)
h2.go_to(7)
# __len__
print(len(h1))
print(len(h2))
# __str__
print(h1)
print(h2)
# __eq__
print(h1 == h2)
# __lt__
print(h1 < h2)
# __le__
print(h1 <= h2)
# __gt__
print(h1 > h2)
# __ge__
print(h1 >= h2)
# __ne__
print(h1 != h2)
# __add__
h1 = h1 + 10
print(h1)
print(h1 == h2)
#__rad__
h1 = h1 + 5
print(h1)
print(h1 == h2)
#_iadd__
h1 = h1 + 1
print(h1)
print(h1 != h2)
