import keyword
'''
변수(Variable)
- 변수란 어떠한 값을 저장하고자 할 때 사용하는 메모리 공간
- 변수는 생성하는 즉시 어떠한 값을 넣어줘야 한다.

변수 사용 예)
score = 10

변수명 생성 규칙
- 영문 문자와 숫자를 사용한다.
- 변수는 대소문자를 구분한다.
- 문자부터 시작해야 하며 숫자부터 시작하면 안된다 !!
- _(under bar)로 시작할 수 있다.
- 특수문자(+, !, @, #, $, %, ^ 등)는 사용할 수 없다.
- 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없다.
* 키워드란 프로그래밍 언어에서 문법적인 용도로 사용되는 것
- 변수명은 가능한 구체적이어야 하고, 해당하는 요소를 명확히 나타내야 한다.

변수명 표기법
- 카멜 표기법, 파스칼 표기법, 헝가리안 표기법, 팟홀 표기법

* 카멜 표기법(Camel Case)
예) carNumberName = "123가4567"
- 맨 처음 문자는 소문자를 표기, 이후 단어의 첫 문자는 대문자로 표기 

* 파스칼 표기법(Pascal Case)
예) CarNumberName = "123가4567"
- 모든 단어 첫 문자를 대문자로 표기

* 헝가리안 표기법(Hungarian Notation)
예) strCarNumber = "123가4567"
    intScore = 100
- 데이터 타입을 명시하여 변수명을 작성하는 방법

* 팟홀 표기법(Pothole case)
예) car_number = 1111
- 단어 사이에 under bar 사용하여 변수명을 작성하는 방법


'''

print(keyword.kwlist);

score = 10;
print(score);

score1 = 20;
print(score1);

Score = 30;
print(Score);

_score = 100;
print(_score);







