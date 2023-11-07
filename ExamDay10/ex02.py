# 숫자 내장 함수
from builtins import enumerate

# abs() : 전달된 인수(정수 또는 실수)의 절대값을 반환
print(abs(10)); print(abs(-10));

'''
divmod()
- 전달된 두 인수를 나누어 몫과 나머지를 한 쌍의 결과로 반환
몫과 나머지는 하나의 튜플(Tuple)로 반환
'''
result = divmod(8,5);
print(result); print(type(result));

# float() : 전달된 인수를 실수로 만들어 반환
print(float(3));
print(float('4'));
print(float(2.4));
print(float('2.4'));

# max() : 전달된 인수 중 가장 큰 값을 반환
result = [1,2,3,4,5];
print(max(result));

# min() : 전달된 인수 중 가장 작은 값을 반환
print(min(result));

# pow() : 전달된 두 인수의 거듭제곱을 반환 (2 ** 4)
print(pow(10,2));
print(pow(10,3));
print(pow(10,4));

'''
sum() : 전달된 리스트나 튜플과 같은 반복가능객체의 합계
'''
list1 = [1,2,3,4,5];
print(sum(list1));

'''
enumerate() 함수
- list와 함께 사용할 수 있고, 리스트에 저장된 요소와 해당
요소의 인덱스가 튜플 형태로 함께 출력됨

출력형태 : (인덱스번호, 값)
'''
list1 = [10,20,30,40,50];
for i in enumerate(list1):
    print(i);

for i in enumerate(['가위','바위','보']):
    print(i);

'''
다음 리스트에서 최대값 최소값 총합, 평균(몫)을 구하세요
'''
arrayList = [10,80,70,60,50,40,30];

print(max(arrayList));
print(min(arrayList));
print(sum(arrayList));
print(sum(arrayList) // len(arrayList));