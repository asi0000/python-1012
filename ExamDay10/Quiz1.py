'''
A ~ Z 까지의 알파벳을 입력받아
대문자는 소문자로 소문자는 대문자로
변경하는 프로그램을 작성하세요

ord() 함수를 이용 => 문자의 유니코드 숫자 값을 리턴하는 함수
'''

# 65~90 대문자, 97~122 소문자
#chr('숫자')는 문자로 반환
# code = print(ord(input("A ~ Z 값의 알파벳을 입력해 주세요. >> ")));
#
# for code in (65, 91):
#     for code1 in (97, 123):
#         if code == range(65, 91):
#             print(chr(code1));
#         else:
#             print(chr(code));

alphaBat = input("알파벳 입력 >>");
if ord(alphaBat) >= 65 and ord(alphaBat) <= 90:
    result = ord(alphaBat) + 32;
    print(chr(result));
elif ord(alphaBat) >= 97 and ord(alphaBat) <= 122:
    result = ord(alphaBat) - 32;
    print(chr(result));