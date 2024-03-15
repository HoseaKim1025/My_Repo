import math
from pprint import pprint
# 당구대 넓이 : 254 * 127 cm
# 공 직경 : 5.73 cm (반지름 : 2.865 cm)

goal = [[2.865, 127-2.865], [127, 127-2.865], [254-2.865, 127-2.865], 
        [2.865, 2.865], [127, 2.865], [254-2.865, 2.865], ]

# white = [63.5, 63.5]
white = [63.5, 127-2.865]
# target = [190.5, 95.25]
# target = [31.75, 111.125]
# target = [127, 95.25]
# target = [63.5, 95.25]
target = [95.25, 127-2.865]

# 흰 구와 목적구 간의 거리
x = target[0] - white[0]
y = target[1] - white[1]
distance = math.sqrt(x**2 + y**2)

# 흰 구를 어떤 포켓에 어떤 각도로 쳐서 넣을지 판단
for i in range(6):

    # 각 포켓과 목적구 간의 거리와 각도
    x1 = goal[i][0] - target[0]
    y1 = goal[i][1] - target[1]
    r = math.sqrt(x1**2 + y1**2)
    if x1 == 0:
        if y1 > 0:
            radian = math.pi / 2
        elif y1 < 0:
            radian = -(math.pi / 2)
    elif x1 < 0:
        radian = math.atan(y1/x1) + math.pi
    else:
        radian = math.atan(y1/x1)
    theta = math.degrees(radian)
    if theta < 0:
        theta += 360
    if i == 1 and not(45 <= theta <= 135):
        continue
    if i == 4 and not(225 <= theta <= 315):
        continue
    # 포켓에 넣기 위한 목적구와의 충돌 위치
    hit_pos = [target[0]-(5.73)*math.cos(radian), target[1]-(5.73)*math.sin(radian)]
    if not(2.865 <= hit_pos[0] <= 254-2.865) or not(2.865 <= hit_pos[1] <= 127-2.865):
        continue
    # 흰 구와 충돌 위치 간의 거리
    x2 = hit_pos[0] - white[0]
    y2 = hit_pos[1] - white[1]
    hit_distance = math.sqrt(x2**2 + y2**2)

    # 칠 수 없는 충돌 위치면 스킵
    # (흰 구와 목적구 간의 거리보다 흰 구와 충돌 위치 간의 거리가 길면 스킵)
    if hit_distance >= distance:
        continue

    if x2 == 0:
        if y2 > 0:
            radian = math.pi / 2
        elif y2 < 0:
            radian = -(math.pi / 2)
    if x2 < 0:
        hit_radian = math.atan(y2/x2) + math.pi
    else:
        hit_radian = math.atan(y2/x2)
    hit_theta = math.degrees(hit_radian)
    
    print()
    print(i)
    print(theta)
    print(hit_pos, hit_theta)