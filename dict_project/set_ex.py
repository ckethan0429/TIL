s1 = set([1,2,3])
print(s1)

s2 = set('hello')   #중복 없고, 순서 없음
print(s2)

s4 = {}
print(type(s4))     # type이 dict

####################################
s1 = set([1,2,3,4,5,6])
s2 = set([7,8,9])

#교집합
print(s1 & s2)
print(s1.intersection(s2)) #같은 표현

#합집합
print(s1 | s2)
print(s1.union(s2))

#차집합
print(s1 - s2)
print(s1.difference(s2))
print(s1[0])