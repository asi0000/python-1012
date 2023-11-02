#
# 컴퓨터가 1 ~ 100 까지의 숫자 중 하나를 랜덤으로 정한다 (이를 알려주지 않습니다.)
# 사용자는 이 숫자를 맞춰야 합니다
# 입력한 숫자보다 정답이 크면 "UP"을 출력
# 입력한 숫자보다 정답이 작으면 "DOWN"을 출력
# 정답을 맞춰면 "축하합니다 정답입니다"를 출력하고
# 지금까지 숫자를 입력한 횟수를 출력하는 프로그램을 작성하세요
#
# (예시)
# 1~100 중 랜덤 숫자 하나를 정합니다.
# 이 숫자를 맞춰주세요.
# 숫자입력 >> 50
# DOWN
# 숫자입력 >> 25
# UP
# 숫자입력 >> 38
# DOWN
# 숫자입력 >> 32
# UP
# 숫자입력 >> 35
# UP
# 숫자입력 >> 37
# DOWN
# 숫자입력 >> 36
# 정답입니다! 7회 만에 맞췄어요.
import random
num = random.randrange(1, 101);

print("1~100 중 랜덤 숫자 하나를 정합니다.")
print("이 숫자를 맞춰 주세요.")

while True:
    num1 = int(input("숫자입력 >> "))
    if num == num1:
        print("정답입니다! {}회 만에 맞췄어요".format())
        break
    elif num > num1:
        print("DOWN");
    if num < num1:
        print("UP");