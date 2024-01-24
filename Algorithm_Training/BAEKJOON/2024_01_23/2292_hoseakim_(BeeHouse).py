n = int(input())
layer = 0
outer_most = 1
while n > outer_most:
    layer += 1
    outer_most += 6 * layer

# layer는 0층부터 시작
# print(f'{n}은 최대값이 {outer_most}인 {layer}번째 층에 있습니다.')

# layer + 1 은 1층부터 시작
print(layer + 1)