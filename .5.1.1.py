class House():
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.H_up = 30 #максимальная высота дома House('ЖК Эльбрус', 30)


    def go_to(self,new_floor):
            if(new_floor > self.number_of_floors or self.number_of_floors >
                    self.H_up or  new_floor < 1):
                print("Такого этажа не существует")
            else:
                 for i in range (int(new_floor)):
                     print(i)



h1 = House('ЖК Горский', 28)
h2 = House('Домик в деревне', 2)
h1.go_to(25)
h2.go_to(7)
