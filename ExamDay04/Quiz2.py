'''
회사 이름이 슬래시('/')로 구분되어 하나의 문자열로 저장되어
있는데 리스트를 생성하여 값을 분리하여 저장하세요

출력결과)
['삼성','LG','네이버']
슬라이싱 사용해 보세요
'''
comp = "삼성/LG/네이버";
print(comp);
comp_list = [comp[0:2],comp[3:5],comp[6:9]];
print(comp_list);

'''
movie_rank 리스트에는 다음과 같이 네 개의 영화 제목이 저장되어 있다
"슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하세요.
'''
movie_rank = ['닥터 스트레인지','스플릿','럭키','베트맨'];
movie_rank.insert( 1, "슈퍼맨");
print(movie_rank);

number_list = [1,2,3];
number_tuple = (1,2,3);
number_list[1] = 20;
print(number_list);
del number_list[1];
print(number_list); #list는 값을 변경할 수 있다.

#number_tuple[1] = 20; #tuple은 값을 변경할 수 없다.
#del number_tuple[1];  #tuple은 삭제도 할 수 없다.
