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
numbers=(input("input number : ")).split()
n1=int(numbers[0])
n2=int(numbers[1])

if n1>n2:
    n1,n2=n2,n1

j=n1
while j<=n2:

    if is_prime(j):
        print(j,end=' ')
    j+=1
