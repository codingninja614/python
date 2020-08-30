name="Sameer malik"
def my_decorator(func):
    def wrapper_func():
        print("**************")
        func()
        print("**************")
    return wrapper_func

@my_decorator
def hello():
    print("hellloooooo!!!")

@my_decorator
def bye():
    print("SEE YA LATER")

@my_decorator
def greet():
    print("Hello "+name)

hello()
print("                                    ")
bye()
print("                                    ")
greet()
