import random

location_name_old = ['이유안', '정진영', '탁호준', '이규석', '김호진',
                    '박주연', '김규림', '조승희', '      ', '신희진',
                    '최영빈', '배원빈', '문재성', '이한솔', '송창용',
                    '이상무', '김민수', '장지현', '      ', '      ',
                    '박성재', '이현복', '한지웅', '김보경', '윤채연',
                    '이남경', '안홍찬', '연상헌']
a = [location_name_old[0:5], location_name_old[5:10],
    location_name_old[10:15], location_name_old[15:20],
    location_name_old[20:25], location_name_old[25:28]]
b = []
print('< 기존 자리 배치도 >')
for i in range(6):
    b.append(a[i][::-1])
c = b[::-1]
for j in range(6):
    print(c[j])
print('[하늘쌤]\n')

a = 0
location_old = list(range(0,28))
location_new = list(range(0,28))

while a == 0:
    b = 0
    random.shuffle(location_new)
    
    for i in range(0,28):
        if location_old[i] == location_new[i]:
            b += 1
    if b == 0:
        a = 1

result = [location_new[0:5], location_new[5:10], 
          location_new[10:15], location_new[15:20],
          location_new[20:25], location_new[25:28]]

location_name_new = []
print('< 다음 자리 배치도 >')
for k in range(0,28):
    x = location_new[k]
    location_name_new.append(location_name_old[x])
result_name = [location_name_new[0:5], location_name_new[5:10],
               location_name_new[10:15], location_name_new[15:20],
               location_name_new[20:25], location_name_new[25:28]]
b = []
for i in range(6):
    b.append(result_name[i][::-1])
c = b[::-1]
for j in range(6):
    print(c[j])
print('[하늘쌤]')
'''
