class Vehicle:


    __COLOR_VARIANTS = ['blue', 'red', 'black','green',  'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)


    def get_model(self):
        return('Модель:',f'{self.__model}')

    def get_horsepower(self):
        return('Мощность двигателя:',f'{self.__engine_power}')

    def get_color(self):
        return('Цвет транспорта:'f'{self.__color}')



    def print_info(self):
        print('Модель',f'{self.__model}'),
        print('Мощность двигателя:',f'{self.__engine_power}'),
        print('Цвет транспорта:',f'{self.__color}'),
        print('Владелец:',f'{self.owner}')
    def set_color(self,new_color):
        for i in  self.__COLOR_VARIANTS:
            if i.upper() == new_color.upper():
                self.__color = new_color
                break
        else:
            print("Нельзя сменить цвет на", f'{new_color}')







class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')



# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('orAnge')
vehicle1.set_color('PurpLe')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
