#과거
'%s %s' %('one','two')

#pyformat
'{} {}'.format('one', 'two')


#fstring
name = "홍길동"
print(f'안녕하세요, {name}')

import random

menu = ['김밥천국', '스타벅스', '부대찌개']
lunch = random.choice(menu)
print("오늘의 점심은 {}입니다.".format(lunch))
print(f'오늘의 점심은 {lunch} 입니다.')

numbers = list(range(1 , 46))
#print(numbers)
lotto = random.sample(numbers, 6)
print(f'오늘의 로또 번호는 {sorted(lotto)}입니다.')
