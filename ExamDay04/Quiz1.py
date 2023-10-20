'''
1. price 변수에는 날짜와 종가 정보가 저장되어 있다
날짜 정보를 제외하고 가격 정보만을 출력하세요.
'''
price = ['20180728',100,130,140,150,160,170];
print(price[1:]);

'''
2. 슬라이싱을 사용해서 홀수만 출력하세요.
'''
nums = [1,2,3,4,5,6,7,8,9,10];
print(nums[0::2]);

'''
3. lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를
모두 갖고 있는 langs 리스트를 만들어 주세요.
'''
lang1 =["c","c++","java"]; lang2 = ["Spring","React","Android"];
langs = lang1 + lang2;
print(langs);