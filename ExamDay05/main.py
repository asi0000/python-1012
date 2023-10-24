# 산술연산자

'''
대입 연산자
- 변수에 값을 저장하기 위해 사용하는 연산자
- 대입연산자는 '=' 는 반드시 왼쪽에 변수가 배치되고 오른쪽에 저장할 값이 배치

복합 대입 연산자
- 복합 대입 연산자를 통해서 연산을 먼저 진행하고 그 결과를 변수에 저장

예)
a += 2
b -= 2
c *= 2
d /= 2
'''

# 두 변수 값 교환
# 중간에 제 3의 변수를 만들어서 변환 시키기
a1 = 10;
b1 = 20;
print("a1의 값 : ", a1); print("b1의 값 : ", b1);
c = a1; # c에 a1값이 들어감 c=10
a1 = b1; # a1에 b1값이 듫어감 a=20
print(a1);
b1 = c; #b1에 c값이 들어감 b1= 10
print(b1);
print("a1의 값 : ", a1); print("b1의 값 : ", b1);

'''
관계연산자
- 두 개의 항을 비교하여 그 결과를 논리(bool) 자료형으로
반환하는 연산
'''
a = 100; b = 200;
print(a > b); # a는 b 보다 크다? False
print(a < b); # a는 b 보다 크다? Ture
print(a >= b); # a는 b 보다 크거나 같다? False
print(a <= b); # a는 b 보다 크거나 같다? Ture
print(a == b); # a와 b는 같다? False
print(a != b); # a는 비와 같지 않다? Ture


'''
논리연산자
- 논리연산자는 관계연산자와 함께 사용되는 연산자로
2개 이상의 항을 논리적으로 연결 할 때 사용한다.

연산자 종류) and, or, not
and, or : 2개 이상의 항을 논리적으로 연결할 때 사용하는 연산자
not : 1개의 항을 논리적으로 처리하는 연산자

AND
A           B           C
False       False       False
False       True        False
True        False       False
True        True        True

OR
A           B           C
False       False       False
False       True        True
True        False       True
True        true        True

NOT
True => False
False => True
'''

# 논리연산자와 관계연산자를 함께 사용하기
print(10 == 10 and 10 != 5);
print(10 > 5 or 10 < 3);
print(not 10 > 5);

'''
삼항연산자
- 참 if 조건식 else 거짓
- 전체를 하나의 식으로 생각해야 한다
- if ~ else 문을 통해서 해결할 수 있는 연산을
한 줄로 간단하게 나타낼 수 있다.

[True] if [값] else [False];
'''
num1 = 20; num2 = 10;
result = num1 if num1 > num2 else num2; #식에서 참이라면 num1이 result에 들어가고 거짓이면 num2가 result에 들어간다
print("두 수중 큰 값 : ", result);

a = int(input("숫자입력 >> "));
print("짝수입니다.") if a % 2 == 0 else print("홀수입니다.");