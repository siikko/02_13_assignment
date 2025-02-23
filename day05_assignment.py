#카운트다운 프로그램
def countdown_loop(n):
    for i in range(n, -1, -1):
        if i == 0:
            print("펑~")
        else:
            print(i)


def countdown_recursion(n):
    if n < 0:
        return
    if n == 0:
        print("펑!")
    else:
        print(n)
    countdown_recursion(n-1)


n = int(input())
#countdown_loop(n)
countdown_recursion(n)

#팩토리얼
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


#피보나치 재귀 & 반복문
def fibonacci_recursion(n) -> int:
    """
    피보나치 수 계산함수 (재귀함수 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)


def fibonacci_loop(n) -> int:
    """
    피보나치 수 계산함수 (반복문 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    n_list=[0 ,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i + 1])

    return n_list[n]

n = int(input())
print(fibonacci_loop(n))
print(fibonacci_recursion(n))


