'''
str_lang = "python"
위 변수를 선언하여 str_lang 문자열에서 첫번째 문자와 세번째 문자를 출력하세요.
'''

str_lang= "python";
print(str_lang[0:3:2]);
print(str_lang[0],str_lang[2]);

'''
자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요
차번호 : 24가 2210
'''
carNumber = "24가 2210";
print(carNumber[4:]);

'''
다음 문자열 중 '홀'만 출력하세요
'''
str_len = "홀짝홀짝홀짝";
print(str_len[0]); #0부터 시작
print(str_len[2]);
print(str_len[4]);
print(str_len[0:5:2]); #오프셋 숫자만큼 건너 뛰면서 출력

