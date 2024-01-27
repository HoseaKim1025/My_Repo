# 문자열 5줄 입력
garo_list = [(list(input())) for _ in range(5)]

# 각 줄마다 길이 측정
garo_len_list = [len(garo_list[i]) for i in range(5)]

# 0번줄보다 길이가 짧은 행에 공백 채워넣기
for i in range(5):
    if garo_len_list[i] < max(garo_len_list):
        for _ in range(max(garo_len_list) - garo_len_list[i]):
            garo_list[i].append('')

# 한 열씩 읽어 한 줄의 문자열로 출력
sero = ''
for j in range(max(garo_len_list)):
    for i in range(5):
        sero += garo_list[i][j]
print(sero)