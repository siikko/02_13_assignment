# SOLID
# Open Closed Principle : 개방 폐쇄 원칙 (확장에는 열려 있고 수정에는 닫혀있는 원칙)
#2중 데코레이터 적용, 성능측정 데코레이터, 디스크립션 데코레이터를 팩토리얼 함수에 적용하시오
import time


#교수님코드
def description_decorator(func):
    def wrapper(*arg):
        print(func.__name__)
        print(func.__doc__)
        r=func(*arg)
        return r
    return wrapper #괄호없어야함.함수호출아님



def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper


def description_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"함수 `{func.__name__}`을 실행합니다.")
        return func(*args, **kwargs)
    return wrapper


@time_decorator
@description_decorator
def factorial_repetition(n) -> int:
    """
    factorial fucntion by loop
    :param n:
    :return: results of factorial operation
    """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


# number = int(input())
# ft = time_decorator(factorial_repetition)
# print(f"{number}! = {ft(number)}")
number = int(input())
print(f"{number}! = {factorial_repetition(number)}")