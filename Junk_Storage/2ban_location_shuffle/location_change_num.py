import random

#셔플 전과 후를 비교하기 위해 두 리스트 생성
location_old = list(range(0,28))
location_new = list(range(0,28))

#가독성을 위해 정리해서 출력
a = [location_old[0:5], location_old[5:10],
     location_old[10:15], location_old[15:20],
     location_old[20:25], location_old[25:28]]
b = []
print('< 기존 자리 배치도 >')
for i in range(6):
    b.append(a[i][::-1])
c = b[::-1]
for j in range(6):
    print(c[j])
print('[하늘쌤]\n')

#셔플 전과 후가 일치하지 않을 때까지 셔플 반복
a = 0
while a == 0:
    b = 0
    random.shuffle(location_new)
    
    for i in range(0,28):
        if location_old[i] == location_new[i]:
            b += 1
    if b == 0:
        a = 1

#가독성을 위해 정리해서 출력
result = [location_new[0:5], location_new[5:10], 
          location_new[10:15], location_new[15:20],
          location_new[20:25], location_new[25:28]]
b = []
print('< 다음 자리 배치도 >')
for i in range(6):
    b.append(result[i][::-1])
c = b[::-1]
for j in range(6):
    print(c[j])
print('[하늘쌤]')
