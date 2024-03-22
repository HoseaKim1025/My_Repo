# 백준 20058 마법사 상어와 파이어스톰 (골드3)
# N(2~6) Q번 시전(1~1000)
N, Q = map(int, input().split())
# 얼음의 양 (0~100)
arr = [list(map(int, input().split())) for _ in range(2**N)]
# 시전 단계
L = list(map(int, input().split()))


