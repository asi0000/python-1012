'''
원을 입력받아 달러로 바꾸어 다음과 같이 출력하세요
$1 = 1100원으로 가정하세요

실행)
원화를 입력하세요 >> 3300
3300원은 $3.0입니다.
'''

won = int(input("원화을 입력해 주세요 >>"));
# 원화 입력값 받기

result = won//1100
print("1$ = 1100원 입니다.")
#가정

print("3300원은 $",float(result),"입니다.");
#달러로 변경 출력