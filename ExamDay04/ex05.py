'''
세트(Set)
- 집합을 표현한다
- 합집합, 교집합, 차집합 등의 연산이 가능
- 세트는 중복값으로 사용할 수 없다.
- 세트에 저장된 값들은 순서가 없다.
- 인덱싱, 슬라이싱 사용불가
- 세트에 특정 값이 있는지 확인을 위해 in 연산자를 사용
 .add(더하기) // .remove(삭제) // .clear(다삭제) // .union(합치기)
'''
s = set(); # 빈 세트 생성
print(s); print(type(s));

fruit = {'apple','banana','orange'};
print(fruit); print(type(fruit));

li = set([1,2,3,4,5,6,7]);
print(li); print(type(li));

# 세트는 추가 삭제 가능
s.add(40); print(s);
s.add(50); print(s);
s.add(60); print(s);
s.add(50); print(s); # 중복된 값이라 입력 x

# 세트 삭제
s.remove(50); print(s);

# 세트 안에 모든 데이터를 삭제
s.clear(); print(s);

# 세트 합치기
set1 = {"a","b","c"};
set2 = {1,2,3};
# union() : 양쪽 모든 데이터를 합친 새로운 set을 반환
set3 = set1.union(set2);
print(set3);