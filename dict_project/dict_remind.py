#1

lunch = {
    '중국집' : '02'
}

#2
lunch = dict(중국집='02')
print(lunch)

#값추가
lunch['분식집'] = '031'
print(lunch)

##
idol = {
    'bts' : {
        '지민' : 25,
        'RM' : 24
    }
}
print(idol['bts']['RM'])


#딕셔너리 반복문
#기본 활용
for key in lunch :
    print(key)
    print(lunch[key])


# .items() - key ,value 둘다가져오기
for key, value in lunch.items():
    print(key, value)

# value만 가져오기
for value in lunch.values():
    print(value)
