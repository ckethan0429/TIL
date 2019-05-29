'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

score_total = 0
for value in score.values():
    score_total += value
score_average = score_total / len(score)
print(f'평균 : {score_average}')
#########################################해설1
total_score = sum(score.values())
average_score = total_score / len(score)
print(average_score)
#########################################해설2


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
class_total = 0
count = 0
for value in scores.values():
    for val in value.values():
        class_total += val
        count += 1
class_avg = class_total / count

print(class_avg)
#########################################해설1











# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
for key, value in cities.items() :
    average_temp = sum(value)/len(value)
    print(f'{key} : {average_temp}')

'''
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
'''


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
count = 0
hot = 0
cold = 0
hot_city = ''
cold_city = ''
for name, temp in cities.items():
    if count == 0 :
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city =name
    else:
       ## 최저온도가 cold보다 추우면, cold 재조정
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        ## 최고온도가 hot 보다 높으면, hot 재조정
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name

    count += 1
print(f'가장 추웠던 곳 : {cold_city} / 가장 더운곳 : {hot_city}')




# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
print(2 in cities['서울'])
if 2 in cities['서울']:
    print('넵')
else:
    print('아니용')