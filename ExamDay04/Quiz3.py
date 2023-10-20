'''
다음 튜플에 저장되어 있는 값 중 네이버를 넥슨으로 변경하세요
'''
intrest = ('삼성','LG','네이버','카카오');
intrest_list = list(intrest);
print(intrest_list); print(type(intrest_list));
del intrest_list[2];
intrest_list.insert(2,'넥슨');
print(intrest_list); print(type(intrest_list));

'''
아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하세요

이름          가격          재고
메로나        300           20
비비빅        400           3
죠스바        250           100
* 이름은 key 가격 재고는 value 값으로
'''
icecream = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}; #대괄호[] 중괄호{} 주의

print(icecream); print(type(icecream));

'''
위의 딕셔너리에 돼지바를 추가해 주세요 가격 800 재고 3개
'''
icecream['돼지바'] = [800,3];   # 쌍 추가 하는 방법 >>>> 변수['키설정'] = [값설정];
print(icecream); print(type(icecream));

