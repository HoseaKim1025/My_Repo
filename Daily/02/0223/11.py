import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(arr)