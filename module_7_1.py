from pprint import pprint
class Product:
    def __init__(self, name:str, weight:float , category:str):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):


        return f'Product({self.name}, {self.weight}, {self.category})'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()

        return products


    def add(self, *products):
        for set in products:
            if set.name not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(set.__str__() + '\n')

            else:
                print(f'Продукт {set.name} уже есть в магазине')


def main():
            

    s1 = Shop()
    p1 = Product('Potato',  50.5, 'Vegitables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    s1.add(p1, p2, p3)
    s1.get_products()
    print(p1)
    print(p2)
    print(p3)


if __name__ == '__main__':
    main()