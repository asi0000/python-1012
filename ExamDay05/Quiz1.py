'''
두 정수를 입력받아 순서를 바꿔서 출력하세요

입력 >> 1
입력 >> 2

출력
2
1
'''

a = int(input("숫자입력 >> "));
b = int(input("숫자입력 >> "));
c = a;
a = b;
b = c;
print(a); print(b);

'''
1. 임의의 두자리 정수 (10 ~ 99)를 입력받아서 십의 자리와 일의 
자리로 분리하여 출력하는 프로그램을 작성하시오

출력 예)
10 ~ 99 사이의 정수를 입력 >> 45
십의자리 : 4
일의자리 : 5

연산자 사용하세요.
'''

a = int(input("10 ~ 99 사이의 정수를 입력 >> "));

print("십의자리 : ", int(a/10)); print("일의자리 : ", int(a%10));