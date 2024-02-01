N = 6
K = 9 # 0~K
data = [7, 2, 4, 5, 2, 3] # 0~9
counts = [0] * (K+1)
temp = [0] * N            # 결과 저장소

# counts 배열에 기록하기
for x in data:
    counts[x] += 1
# counts 누적합 구하기
for i in range(1, K+1):
    counts[i] += counts[i-1]
# data의 마지막 원소부터 정렬하기...
for i in range(N-1, -1, -1): # N-1 -> 0
    counts[data[i]] -= 1 # 개수를 인덱스로 변환 (남은 개수 계산)
    temp[counts[data[i]]] = data[i]
print(*temp)

