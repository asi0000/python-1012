'''
해당 월을 입력받아 계절 이름이 출력되는 프로그램을 작성

12, 1, 2 : 겨울
3, 4, 5 :  봄
6, 7, 8 : 여름
9, 10, 11 : 가을
'''

weater = int(input("월 입력 >> "))
if weater == 12 or weater == 1 or weater == 2:
    print("겨울")
elif weater == 3 or weater == 4 or weater == 5:
    print("봄")
elif weater == 6 or weater == 7 or weater == 8:
    print("여름")
elif weater == 9 or weater == 10 or weater ==11:
    print("가을")