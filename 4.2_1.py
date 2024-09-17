def test_function():
    print()
    def inner_function():
        print(f"Я в области видимости функции ,test_function()")
inner_function() # вызов функции из локального сектора в глобальный вызывает ошибку
test_function()


