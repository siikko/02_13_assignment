#assingment
# v3.8) kw
def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(f'Function Name : {func.__name__}')
        print(f'Function Arguments : {args}')
        print(f'Function keyword Arguments : {kwargs}')
        result=func(*args,**kwargs)
        return result
    return wrapper #항상정해져있음
@log_decorator
def greet(name, greeting="안녕하세요",age=None):
    return f"{greeting}, {name}(age:{age})"if age else f"{greeting}, {name}"
print(greet("인하"))
print(greet("인상","안녕"))
print(greet("James","Hello"))
print(greet("Gonzales",greeting="Hola"))
print(greet("Nakamura",greeting="Gonniziwa",age=29))