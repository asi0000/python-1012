'''
while문을 이용해 두 개의 주사위를 던졌을 때 나오는 눈을
출력하고 눈의 합이 5가 아니면 계속 주사위를 던지고
눈의 합이 5이면 실행을 멈추세요
종료가 되면 루프를 돈 만큼 주사위 합을 출력해 주세요.
'''
import random

i = 0;
sum = 0;

while True:
    a = random.randint(1, 6);
    b = random.randint(1, 6);
    input("주사위를 던지시겠습니까? enter를 누르면 주사위가 던져집니다.")
    if a + b == 5:
        i = i + 1
        sum = sum + a + b
        print("주사위 던지기를 멈춥니다. 던지기 총합은",sum,"입니다");
        break;
    else:
        print("주사위를 다시 던져야 합니다.")

# sum = 0;
# while True:
#     a = random.randint(1,6);
#     b = random.randint(1,6);
#     sum = a + b;
#     print("{} + {} = {}".format(a,b,(a+b)));
#     if sum == 5:
#         break;