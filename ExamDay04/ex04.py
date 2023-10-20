'''
딕셔너리(Dict)
- 키(key), 값(value)이 한쌍이 하나의 대응 관계를 가지고 있다.
- 키(key)값은 중복, 수정이 불가능.
- 값(value)은 중복, 수정이 가능하다.
- 사칙연산 불가능.

형식)
{key1:value1, key2:value2, key3:value3,...}
'''
dic = {'name':'안상현','phone':'01097188375','birth':'0119'};
print(dic); print(type(dic));

# value 값에 list를 넣을 수 있다.
a = {'a':[1,2,3,4,5],'b':['.../...']};
print(a); print(type(a));

# 딕셔너리 쌍 추가
a['b'] = [4,5,60];
a['c'] = 20;
print(a);
a['d'] ={'10':40};
print(a);

# 딕셔너리 요소 삭제
# 딕셔너리 삭제는 키값으로 접근하여 삭제해야 한다.
del a['b'];
print(a);

# 해당 key값이 딕셔너리에 존재하는지 확인하는 방법
print('c' in a);

# 딕셔너리 키 값만 추출하기
print(a.keys());
