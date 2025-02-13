def squares(*n) -> list: #가변매개변수: 인자의 개수가 정해져 있지 않을 때
    """
    넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    """
    print(n)
    return [pow(i, 2) for i in n]
    #return n * n


def run_function(f, *number) -> list:
    return f(*number)

print(squares(7, 5, 2,-9))
#print(run_function(squares, 9, 10))





numbers = ["7", "-11", "3"]
print(sum(map(int, numbers)))

# numbers = ["7", "-11", "3"]
# hap = 0
# for number in numbers:
#     hap = hap + int(number)
# print(hap)