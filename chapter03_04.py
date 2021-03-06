# Chapter03_04
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) #불변 immutable
# 용도: 중요한 데이터가 있어서 변경되면 안될 때 ex. 기준값, 정보

# 선언
a = ()
b = (1,) # 원소가 하나일 때 int로 인식 안하게 하기 위해서 콤마 찍어야 함
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱 - 거의 리스트랑 똑같은듯
print('>>>>>')
print('d-', d[1])
print('d-', list(e[-1][1])) # 리스트로 변환가능, 이 경우 리스트처럼 수정 및 삭제 가능

# 수정 x
#d[0] = 1500

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

# 튜플 연산 - 연산을 통한 데이터 길이 변화는 용인
print('>>>>>')
print('c+d', c+d)
print('c*3', c*3)

# 튜플 함수
a = (5,2,3,1,4)
print('a -', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 패킹 언패킹
t = ('foo', 'baz', 'qux', 'bar')
# 패킹 = 인덱싱이 이루어짐, 하나로 묶음
print(t)
print(t[0])
print(t[-1])

# 언패킹
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 하나로 되어있던 튜플을 괄호로 각각 나누는 것

t2 = 1, 2, 3 # 이렇게 괄호 없이 하는 것도 튜플
t3 = 4,
x1, x2, x3 = t2 # 언패킹
x4, x5, x6 = 4, 5, 6 # 동시 할당, 언패킹: 각각의 원소에 대입이 되도록 하는 것
