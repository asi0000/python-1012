'''
자료형
- int(정수)
- float(실수)
- complex(복소수)
- str(문자열)
- bool(논리)
'''

num1 = 10; #양의 정수
num2 = -10; #음의 정수
num3 = 0;
num4 = 20;

print(num1);
print(num2);
print(num3);
print(num4);
print(type(num1));
print(type(num2));
print(type(num3));
print(type(num4));

# 파이썬 에서는 기본적으로 원하는 값을 크기에 제한없이 사용가능
num5 = 99999999999999999999999999999999999999999999999999999
print(num5);
print(type(num5));

# 10진수를 2진수, 8진수, 16진수로 변환
num1_int = 10;
print(bin(num1_int)); # 2진수로 변환
print(oct(num1_int)); # 8진수로 변환
print(hex(num1_int)); # 16진수로 변환

'''
실수(float)
- 소수점이 있는 숫자를 실수라고 한다.
'''
num1_float = 10.0;
print(num1_float);
print(type(num1_float));
num2_float = 3.141592;
print(num2_float);
print(type(num2_float));

# 문자열(str)
a_str = "Good Student";
b_str = 'Bad Student';

print(a_str);
print(type(a_str));
print(b_str);
print(type(b_str));

# 여러줄 문자열로 출력하기
c_str = '''asdfasdfasdfasdfasdfsadfasdfasdfasdfas
dfasdfasdfasdfasdfsadfasdfasdfasdfasdfasdfasdfasdf
asdfsadfasdfasdfasdfasdfasasdfasdfasdfasdfa
sdfsadfasdfasdfasdfasdfasdfasdfasdfasdfsadfasdf
asdfasdfasdfasdfasdfasdfasdfasdf''';
print(c_str);
print(type(c_str));

'''
논리(bool)
- True, False 값을 가질 수 있다
- 숫자 0, 빈 문자열, [] 빈 리스트 모두 False로 반환
'''
bool_a = True;
bool_b = False;
print(bool_a);
print(type(bool_a));
print(bool_b);
print(type(bool_b));
a = 0; #False
b = 1; #True
print(bool(a)); print(bool(b));
null_str = ""; #False
print(bool(null_str));
null_list = []; #False
print(bool(null_list));

'''
복소수(Complex)
- 실수부와 허수부를 구분하여 표현할 수 있다.
'''

a1 = 2 + 3j;
print(type(a1)); print(a1);

# 기본적인 사칙연산
a1 = 20;
b1 = 10;
print("덧셈결과 : ", (a1 + b1));
print("뺄셈결과 : ", (a1 - b1));
print("곱셈결과 : ", (a1 * b1));
print("나눗셈 몫 : ", (a1 / b1));
print("나눗셈 나머지 : ", (a1 % b1));
print("나눗셈 몫만 출력 : ", (a1 // b1)); #파이썬에서만 가능 //
print("2를 4번 제곱한 결과 : ", (2 ** 4)); #파이썬에서만 가능 **
