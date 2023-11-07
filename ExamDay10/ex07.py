'''
메소드(Method)
- 특정 객체(Object)가 가지고 있는 함수(function)를 의미
- 함수는 독립적으로 호출할 수 있지만 메소드는 특정 객체를
통해서만 호출 가능

* 함수와 메소드의 차이점
- 함수는 독립적으로 정의되므로 이름으로만 호출이 가능
- 메소드는 이름으로만 호출되지 않음, 정의된 클래스의 참조에 의해 클래스를 호출해야 함!!
'''

'''
count() 메소드
- 문자열 내부에 포함된 특정 문자열의 개수를 반환하는 메소드
'''
str1 = '''내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'''
print(str1.count('기린'));
print(str1.count('기린',15)); #글자 찾는데 몇번째 부터인지

fruits = ['Apple','Banana','Mango','Pineapple','Coconut','Orange','Strawberry','Remon','Mango'];
print("Mango 개수 : ", fruits.count('Mango'));
print("Banana 개수 : ", fruits.count('Banana'));
print("갈비 개수 : ", fruits.count('갈비')); # 찾고자 하는 문자열이 없으면 0을 반환

# find() 메소드
# 문자열 내부에 포함된 특정 문자열을 찾고자 할 때 사용
s = 'Hello World';
print(s.find('o')); # 문자열이 위치한 인덱스 값을 반환
print(s.find('l'));
print(s.find('a')); # 찾고자 하는 문자열이 없으면 -1을 반환

s1 = "best of best";
# 검색 범위를 지정해서 사용가능
#('찾는문자열', '몇 번째 부터 찾을건지')
print(s1.find("best",5)); #같은 글자가 있을 때 사용
