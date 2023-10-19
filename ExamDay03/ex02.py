'''
파이썬 정수 변환 - int()
파이썬 실수 변환 - float()
파이썬 문자열 변환 - str()
파이썬 문자 변환 - chr()
파이썬 bool 변환 - bool()
'''

#...()에 넣으면 변환이 됨
#true = 1, false = 2

# 파이썬 int 타입 변환
a1 = 10;
print("정수를 정수로 변환 : ", int(a1));

a2 = 3.141592;
print("실수를 정수로 변환 : ", int(a2));

a3 = int(True);
print("bool을 정수로 변환", a3);

a4 = int(False);
print("bool을 정수로 변환", a4);

# 문자와 문자열은 정수형(int)으로 변환 불가능
# a5 = int('a');
# a6 = int("문자열");
# print(a5);
# print(a6);

'''파이썬 float 타입 변환'''
# 실수를 실수로 변환
b1 = float(3.141592);
print("실수를 실수로 변환 : ", b1);

# 정수를 실수로 변환
b2 = float(10);
print("정수를 실수로 변환 : ", b2);

# bool을 실수로 변환
b3 = float(False);
print("bool을 실수로 변환 : ", b3);

b4 = float(True);
print("bool을 실수로 변환 :", b4);

# b5 = float("안상현");
# print(b5);

''' str 타입 변환 '''
c1 = str(10);
print("정수를 문자열로 변환 : ", c1);
print(type(c1));

c2 = str(3.141592);
print("실수를 문자열로 변환 : ", c2);
print(type(c2));

c3 = str(True);
print("bool을 문자열로 변환 : ", c3);
print(type(c3));

#아스키코드표
# https://stepbystep1.tistory.com/10

''' chr 타입 변환 '''

chr_a = chr(65);
print(chr_a);
print(type(chr_a));

chr_b = chr(66);
print(chr_b);
print(type(chr_b));

chr_c = chr(97);
print(chr_c);
print(type(chr_c));




