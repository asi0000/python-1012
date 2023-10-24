'''
숫자를 입력받아 그 수의 절대값을 구하세요

입력 >> -5
출력 >> 5

입력 >> 5
출력 >> 5
'''

num1 = int(input("입력 >> "));
if num1 != 5:
    print("출력 >>",-num1)
else:
    print("출력 >>",num1);
print();

num2 =int(input("입력 >> "));
if num2 == 5:
    print("출력 >>",num2)
else:
    print("출력 >>",-num2);

'''
 수를 입력받아 짝수인지 홀수인지 판단하세요
 짝수면 짝수입니다 출력
 홀수면 홀수입니다 출력
'''

int1 =int(input("수 입력 >>"));
if int1 % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다");