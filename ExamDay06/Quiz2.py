'''
시험점수를 입력받아
90 ~ 100점은 A,
80 ~ 89점은 B,
70 ~ 79점은 C,
60 ~ 69점은 D,
나머지 점수는 F를 출력하는 프로그램을 작성하시오.
'''

score = int(input("시험점수를 입력하세요 >> "));
if score > 89:
    if score <= 100:
     print("A 입니다.")
elif score > 79:
    if score < 90:
     print("B 입니다.")
elif score > 69:
    if score < 80:
     print("C 입니다.")
elif score > 59:
    if score < 70:
     print("D 입니다.")
else:
     print("F 입니다.")

