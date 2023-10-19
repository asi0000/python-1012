''' 다양한 형태의 리스트 '''
a = []; #빈리스트
b = [1, 'a', 'b', "갤럭시"];
c = [1,2,3];
d = ['apple', 'banana', '포도', "딸기"];
e = [1,2,['커피','라떼']];

print("list a : ", a);
print("list b : ", b);
print("list c : ", c);
print("list d : ", d);
print("list e : ", e);

# 리스트 인덱싱 (시작은 [0])(마지막은 [-1])(들여쓰기 조심하기)
arrays = [10,20,30,40,50];
print("list 1번째 요소 : ", arrays[0]);
print("list 2번째 요소 : ", arrays[1]);
print("list 3번째 요소 : ", arrays[2]);
print("list 4번째 요소 : ", arrays[3]);
print("list 5번째 요소 : ", arrays[4]);
print();
print("list 마지막 요소: ", arrays[-1]);
print("list 4번째 요소:", arrays[-2]);
print("list 3번째 요소:", arrays[-3]);
print("list 2번째 요소:", arrays[-4]);
print("list 1번째 요소:", arrays[-5]);

'''
리스트 슬라이싱
''' # 마이너스 사용시 마지막 마이너스에는 -1이 붙기 때문에 주의
score = [100,200,300,400,500];
print(score[0:3]);
print(score[-4:-1]);