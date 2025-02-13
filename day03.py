# Assignment
# v2.6) while 안쪽의 조건문을 줄이세요.
import random

drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삽겹살", "양꼬치"]
prices=[50000,30000,5000,7500]
# amounts=list()
# for i in range(len(drinks)):
#     amounts.append(0)
amounts=[0 for i in range(len(drinks))]
print(amounts)
drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"
drinks.append("데킬라")
snacks.append("소금")

total_price=0
def print_menu_total_price(n):
    global total_price
    print(f'{drinks[n]}에 어울리는 안주는 {snacks[n]} 입니다')
    print(f'가걱 : {prices[n]}')
    amounts[n]=amounts[n]+1
    total_price=total_price+prices[n]


menu_list = '다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}  '
menu_list = menu_list + f'{len(drinks)+1}) 아무거나  {len(drinks)+2}) 종료 : '

while True:
    menu = int(input(menu_list))
    if 1 <= menu <= len(drinks):
        print_menu_total_price(menu - 1)
    elif menu == len(drinks)+1:
        random_index = random.randint(0, len(drinks)-1)
        print(f'{drinks[random_index]}에 어울리는 안주는 {snacks[random_index]} 입니다')
    elif menu == len(drinks)+2:
        print(f'다음에 또 오세요')
        break

for k in range(len(drinks)):
    if amounts[k] !=0:
        print(f"주류명 : {drinks[k]} 수량 : {amounts[k]}  단가 : {prices[k]} 소계 : {amounts[k]*prices[k]}")
print(f"총 금액 : {total_price}원")