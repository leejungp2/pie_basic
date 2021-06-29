#Chapter 09-1
# 파일 읽기 및 쓰기

# 읽기 모드 r, 쓰기모드 w, 추가 모드 a(append) 텍스트 모드 t, 바이너리 모드 b
# 상대 경로('../, ./')-현재 폴더의 위치, 절대 경로('C:\Django\example...')

# 파일 읽기(read)
# 예제1 (내부함수 오픈)
# f = open('C:\\pie_basic\\resource\\it_news.txt') 절대 경로
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close
f.close()

# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제3
# read(): 전체 읽기, read(10): 10Byte 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    # 마지막에 읽은 곳이 어디인지를 기억하고 있음
    f.seek(0,0) # 초기화
    c = f.read(10)
    print(c)

print()

# 예제4
# readline: 한 줄 씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)

print()

# 예제5
# readlines: 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end = '')

# 파일 쓰기 (write)
# 예제1
with open('./resource/contents.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contents.txt', 'a') as f:
    f.write('I love python2\n')

# 예제3
# writelines: 리스트->파일
with open('./resource/contents.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n']
    f.writelines(list)

# 예제4
with open('./resource/contents.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
