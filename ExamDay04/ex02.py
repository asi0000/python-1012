'''
튜플(tuple)
- 튜플은 몇가지 특징을 제외하고 리스트와 거의 비슷하다.
- 프로그램이 실행되는 동안 그 값이 변경되면 안돼는 경우 튜플을 사용

리스트와 차이점
- 리스트는 []로 둘러싸지만 튜플은 ()로 둘러싼다.
- 리스트는 생성, 수정, 삭제가 가능
 튜플은 요소 값을 바꿀 수 없다.
'''

tuple_exam = (1,2,3);
print(tuple_exam); print(type(tuple_exam));

# 튜플의 다양한 모습
t1 = (); # 빈튜플
t2 = (1,); #  튜플은 1개의 요소만 가질 때 요소 뒤에 콤마를 반드시 붙여야 한다.
print(t2); print(type(t2));
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','g',(1,2,3));
print(t1); print(t2); print(t3); print(t4); print(t5);
print(type(t1)); print(type(t2)); print(type(t3));
print(type(t4));  print(type(t5));

tuple1 = (1,2,'a','b');
# 튜플 인덱싱
print(tuple1[0]);
print(tuple1[1]);
print(tuple1[2]);
print(tuple1[3]);

# 튜플 슬라이싱
print(tuple1[1:3]); print(tuple1[0:2]);

# 튜플 덧셈
tuple2 = (3,4);
result = tuple1 + tuple2;
print(result);

# 튜플 곱하기
tuple3 = (3,4);
print(tuple3 * 3);

# 튜플 길이 구하기
tuple_len = (1,2,'a','b');
print("tuple_len 튜플 길이 : ", len(tuple_len));

a = 1,2,3,4,5;
b = 'o',[1,2],'apple','coffee';
print(a); print(type(a));
print(b); print(type(b));