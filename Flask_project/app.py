from flask import Flask, render_template, request
import random

app = Flask(__name__)
##여기까지 고정

@app.route('/')
def index():            #뷰 함수
    return 'bye world!'

@app.route('/hello')
def hello():
    return '반갑습니다.'

@app.route('/greeting/<name>')
def greeting(name):
    return f'반갑습니다.{name}님'

@app.route('/cube/<int:num>')
def cube(num):
    result = num **3
    return str(result)

####
#'/lunch/3'으로 요청이 들어왔을 때
# 메뉴 리스트에서 랜덤으로 인원 수 만큼 메뉴 골라서
# 출력해주기
@app.route('/lunch/<int:total_people>')
def menu(total_people):
    menu_list = ['김치찌개','된장찌개','비빔밥','짜장면','짬뽕','볶음밥']
    sel_num = random.sample(menu_list, total_people)
    return str(menu_list)

@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요!</h1>'

@app.route('/html_line')
def html_line():
    return '''<h1>안녕하세요!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>'''

@app.route('/html_render')
def html_render():
    return render_template('index.html')

@app.route('/html_name/<name>')
def html_name(name):
    return render_template('hello.html', name = name)


@app.route('/html_num/<int:num>') #string으로 값을 하면 밑에서 형변환해줘야함
def html_num(num):
    num_count = num**3
    return render_template('num.html', num=num , num_count = num_count)


# 저녁메뉴 랜덤 뽑기
# /dinner로 요청이 들어왔을 떄
# 저녁메뉴에서 하나를 뽑아서 이미지와 메뉴 이름을 응답해주자.
# 출력예시
# 오늘의 저녁은 ??? 입니다.
# ??? 이미지
@app.route('/dinner') #string으로 값을 하면 밑에서 형변환해줘야함
def dinner():
    menu_list = ['김치찌개', '된장찌개', '비빔밥', '짜장면', '짬뽕', '볶음밥']
    image_list = ['http://recipe1.ezmember.co.kr/cache/recipe/2016/10/11/6dcc7dd9434577d65a9acb8ec97043591.jpg',
                  'http://recipe1.ezmember.co.kr/cache/recipe/2017/04/26/ddd495fd432955701068e1a21a0d33211.jpg',
                  'http://recipe1.ezmember.co.kr/cache/recipe/2015/06/01/0467fec40dc5df750f026e7a87b4b1261.jpg',
                  'http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1214/IE002069160_STD.jpg',
                  'http://food.chosun.com/site/data/img_dir/2012/08/08/2012080802054_0.jpg',
                  'http://recipe1.ezmember.co.kr/cache/recipe/2019/03/14/4c1d1794eb908c1bfec012999d7b43cc1.jpg']
    index = random.sample(range(0,7), 1)
    print(index[0])


    return render_template('dinner.html', menu_list=menu_list[index[0]] , image_list = image_list[index[0]])


@app.route('/lotto')
def lotto():
    number_list = list(range(1,46))
    lucky = random.sample(number_list, 6)

    return render_template('lotto.html', lucky = lucky)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

#########################get방식##########################
@app.route('/ping')
def ping():
    return render_template('ping.html')

# ping.html으로 넘긴후 'name' = 입력값('핑핑핑핑') -> /pong밑에서 받음.

@app.route('/pong')
def pong():
    #username = request.args['name']
    username = request.args.get('name')
    return render_template('pong.html', username=username)

###################post방식####################################
@app.route('/ping_new')
def ping_new():
    return render_template('ping_new.html')

@app.route('/pong_new', methods = ['POST'])
def pong_new():
    username = request.form.get('name')
    return render_template('pong_new.html', username=username)

######################실습#####################################
@app.route('/god_ping')
def god_ping():
    return render_template('god_ping.html')

@app.route('/god_pong')
def god_pong():
    username = request.args.get('name')
    character = ['멍청함','똑똑함', '똘끼', '귀여움', '섹시함', '잘생김', '못생김','자상함','의리','카리스마','허세','병신력','애교','재력']
    choice_character = random.sample(character, 3)
    return render_template('god_pong.html', username= username, choice_character=choice_character)


#파이썬 파일이 직접실행된 코드라면 if문 코드를 동작한다.
if __name__ == '__main__':
    app.run(debug = True)
