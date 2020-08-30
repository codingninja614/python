name="sameer"
def greeting(func):
    def wrapper_func():
        print("***************************")
        func()
        print("***************************")
    return wrapper_func
@greeting
def hello():
    print("hello")
@greeting
def bye():
    print("SEEE YAAAAAAAA LATERRRRRRRRRRR!")
@greeting
def greet():
    print("hello"+name)

hello()
print("                           ")
bye()
print("                           ")
greet()
