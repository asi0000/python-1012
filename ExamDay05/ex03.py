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

# 세 수의 합계 구하기
kor = 90; mat = 40; eng = 70;
sum = kor + mat + eng;
print("국영수 점수 총 합 : ", sum);
avg = sum // 3
print("국영수 점수 평균 : ", avg);

'''
+= : 숫자를 더한 후 대입
-= : 숫자를 뺀 후 대입
*= : 숫자를 곱한 후 대입
/= : 숫자를 나눈 후 대입
//= : 숫자를 나눈 후 그 몫만 대입
%= : 숫자를 나눈 후 그 나머지만 대입
**= : 숫자를 제곱한 후 대입
'''
num = 100;
print(num);

num += 10; print(num);
num *= 2; print(num);
num /= 2; print(num);
num *= 3; print(num);

greet = "안녕";
greet = greet + '하세요';
print(greet);
greet *= 2;
print(greet);