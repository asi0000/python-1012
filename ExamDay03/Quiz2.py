
'''
주민번호는 다음과 같이 구성된다
XXXXXX-XXXXXXX
왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
주민번호를 입력받아 형태를 바꿔 출력하시오

입력
주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다.
(입력값은 가상의 주민번호이다.)
ex)110011-0000000

출력
'-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.
실행 예)
주민등록번호입력 >> 000907-1121112

출력결과
0009071121112
'''
num = input("주민등록번호입력 >> ");

result=(num[:6])+ (num[7:]);
print(result);

# result 로 먼저 계산하고 (-)빼고 계산할때 앞 그룹 뒷 그룹 나눠서 사용하기
#
# print로 출력하기

