'''
두 정수 a와 b를 입력 받아서
두 정수의 크기를 비교하여 왼쪽 수가 크면 > 출력
오른쪽 수가 크면 < 를 출력
두 수가 같다면 = 를 출력
'''

a = int(input("숫자입력 >> "))
b = int(input("숫자입력 >> "))
if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("=")
#else:
#     print("=")