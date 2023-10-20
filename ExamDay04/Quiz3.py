'''
다음 튜플에 저장되어 있는 값 중 네이버를 넥슨으로 변경하세요
'''
intrest = ('삼성','LG','네이버','카카오');
intrest_list = list(intrest);
print(intrest_list); print(type(intrest_list));
del intrest_list[2];
intrest_list.insert(2,'넥슨');
print(intrest_list); print(type(intrest_list));

d