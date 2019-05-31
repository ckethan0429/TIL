from flask import Flask, request, render_template
import json
import requests
import random
app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')

    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = response.json()

    #### 당첨번호 6개 가져오기
    # winner= []
    # for i in range(1,7):
    #     winner.append(lotto[f'drwNo{i}'])

    # list comprehension
    winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]

    ### 1. 내 번호 리스트 만들기
    mylotto = list(random.sample(range(1,46), 6))
    input_lotto = []
    for i in range(6):
        input_lotto.append(int(request.args.get(f'input_lotto{i}')))
    ### 2. (도전) 내번호를 lotto_check에서 입력해서 넘어온 6개 번호로 만들기

    ### 당첨번호와의 교집합
    matched = len(set(winner) & set(input_lotto))
    rank = 0
    print(matched)
    print(winner)
    print(input_lotto)
    ### 조건에 따라 1등부터 꽝까지 결과값을 lotto_result로
    if matched == 6:
        rank = 1
    elif matched == 5 and lotto["bnusNo"] in input_lotto:
        rank = 2
    elif matched == 5:
        rank = 3
    elif matched == 4:
        rank = 4
    elif matched == 3:
        rank = 5
    else:
        print('꽝입니다.')

    return render_template('lotto_result.html',lotto_round=lotto_round, winner=f'{winner}+{lotto["bnusNo"]}', input_lotto=f'{input_lotto}', rank =f'{rank}등 입니다')


if __name__ == '__main__':
    app.run(debug=True)
