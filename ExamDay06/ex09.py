treeHit = 0;

while treeHit < 10:
    treeHit = treeHit + 1;
    print("나무를  {}번 찍었습니다.".format(treeHit));
    if treeHit == 10:
        print("나무넘어갑니다.")


'''
숫자를 입력받아 입력받은 숫자만큼 반복문을 실행하세요.
1부터 입력받은 숫자를 전부 출력하면 됩니다.
'''

num = int(input("숫자를 입력하세요 >> "))

a = 0;
while a < num:
    a = a + 1;
    print(a)