def is_prime(num)->bool: #타입힌트
    """
    함수에 대한 설명
    :param num:
    :return:
    """
    if num >= 2:
        i=2
        while i<(int(num**0.5)+1):

            if num%i==0:
                return False
            i+=1

    else:
        return False
    return True

help(is_prime) #함수에 대한 설명 출력
n=int(input("input number : "))

if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")