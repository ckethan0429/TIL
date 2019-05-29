import random
import requests
import json
from pprint import pprint


url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860'
res = requests.get(url)
lottery = res.json()
#pprint(lottery)

winner = []
for i in range(1, 7):
    winner.append(lottery[f'drwtNo{i}'])
total_count = 0
count_1 =0
count_2 =0
count_3 =0
count_4 =0
count_5 =0
count_else = 0
while(True):

    total_count += 1
    if(total_count % 100000 ==0):
        print(total_count)


    bonus = lottery['bnusNo']
    #print(winner)
    #print(bonus)

# 내가 자동으로 산 복권번호와 당첨번호(winner) 교집합 개수 비교 를 통해 등수 매기기
    cklotto = random.sample(range(1,45),6)
    #print(f'당첨 번호    : {winner}')
    #print(f'내가 산 로또 : {cklotto}')

    set_cklotto = set(cklotto)
    set_winner = set(winner)
    #print(set_cklotto)
    #print(set_winner)
    intersection = set_winner & set_cklotto
    gap = list(set_winner - set_cklotto)
    #print(gap[0])
    if len(intersection) == 6:
        #print('1등')
        count_1 += 1

        break
    elif len(intersection) == 5:
        if(gap[0] == bonus):
             #print('2등')
             count_2 += 1
        else:
             #print('3등')
             count_3 += 1

    elif len(intersection) == 4:
        #print('4등')
        count_4 += 1
    elif len(intersection) == 3:
        #print('5등')
        count_5 += 1
    else:
        #print('다시는 하지마세요')
        count_else += 1


print(f'1등 : {count_1}, 2등 : {count_2}, 3등 : {count_3}, 4등 : {count_4}, 5등 : {count_5}, 떨거지 : {count_else}, total :{total_count}' )