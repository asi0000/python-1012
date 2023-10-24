fruit = ['사과','포도','바나나','체리'];
print(fruit);
# 리스트의 끝에 추가하기
fruit.append('배');
print(fruit);

# 리스트 원하는 위치(index)에 값을 추가하기
fruit.insert(1,'수박');
print(fruit)

# 리스트 삭제 : del, pop()
#pop() 지정한 위치 삭제
#del 범위 삭제
fruit.pop(); #공백시 마지막 값 삭제
print(fruit);
fruit.pop(4);
print(fruit);

del fruit[0];
print(fruit);
del fruit[0:2]; # 범위지정삭제
print(fruit);

fruit.append('수박');
fruit.append('포도');
fruit.append('바나나');
print(fruit);

# 리스트 안에 모든 데이터를 삭제
fruit.clear();
print(fruit);

arrays = [10,20,30,40,50];
print(arrays)
# 리스트 값 수정
arrays[2] = 300;
print(arrays);

# 리스트에서 여러개의 값을 수정할 수 있다.
remove_arrays = [10,20,'사과','딸기','포도'];
remove_arrays[2:4] = ['apple','strawberry'];
print(remove_arrays);

# 리스트 뒤집기
close = [10,20,30,400,2];
close.remove();
print(close);




