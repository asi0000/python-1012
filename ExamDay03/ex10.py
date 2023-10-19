'''
리스트 요소 추가
- 리스트에 새로운 값을 추가할 때는
  append() 메소드와 insert()메소드를 사용할 수 있다.

*append() : 리스트에 항상 마지막 요소로 추가.
*insert() : 원하는 위치에 값을 넣을 수 있다. (뒤 값은 한칸씩 밀린다.)
'''
scores = [50,40,30];
scores.append(10);
print(scores);
scores.append("추가");
print(scores);

scores.insert(1,90);
print(scores);

# 리스트 값 삭제
# pop() 함수는 지정한 위치의 값을 삭제,
# 위치를 지정하지 않으면 맨 끝에 있는 데이터를 삭제
scores.pop(2);
print(scores);
scores.pop();
print(scores);

# del 함수를 사용해 리스트 요소 삭제
# del : 위치 또는 범위를 지정해서 삭제
del scores[1];
print(scores);
del scores[0:2];
print(scores);

arrays = [10,20,30,40,50];
arrays.clear();
print(arrays);






