def decorator(func):
    def wrapper():
        print("before funtion runs")
        func()
        print("after funtion runs")
    return wrapper


@decorator
def greet():
    print("hello form shan ")
greet() 


