'''
중첩된 리스트에서 슬라이싱 하기
'''
arrValue = [10,20,['커피','바나나','포도']];
print(arrValue[0]);
print(arrValue[1]);
print(arrValue[2]); # 리스트안에 포함된 리스트는 다 나온다.
print(arrValue[2][0]); # 리스트안에 있는 리스트를 가져올 땐 []뒤에 []를 붙인다.
print(arrValue[2][1]);
print(arrValue[2][2]);
print(arrValue[2][0:2]); # 커피가 0 바나나1 포도2
print(arrValue[2][:3]); # 마지막 값-1 되야해서 다 입력 되려면 3이 맞음.
print(arrValue[2][-3:]);