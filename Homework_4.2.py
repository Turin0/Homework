def test_function():
    def inner_function():
        print('Я в области видимости test_function')
    inner_function()


# inner_function() # Данная функция находится в пространстве имен функуции test_function поэтому программа не видит её.