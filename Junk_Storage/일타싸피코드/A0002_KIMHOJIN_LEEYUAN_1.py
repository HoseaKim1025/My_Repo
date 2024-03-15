import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'A0002_1149888'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.






    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    targetBall_x = balls[1][0]
    targetBall_y = balls[1][1]

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian
    
    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 90
        else:
            angle = 270

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180
    
    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90
        
    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width**2 + height**2)
    print('두 구의 거리 :', distance)
    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.5

    # 목적구와 흰공 간의 x좌표 거리 width
    # 목적구와 흰공 간의 거리 distance
    # 흰공을 쳐서 목적구의 좌표로 보낼 수 있는 각도 angle

    # goal_list = [[2.865, 2.865], [127, 0], [254-2.865, 2.865], 
    #              [2.865, 127-2.865], [127, 127], [254-2.865, 127-2.865]]
    # goal_list = [[2.865, 2.865], [128, 0], [256-2.865, 2.865], 
    #              [2.865, 128-2.865], [128, 128], [256-2.865, 128-2.865]]
    # goal_list = [[0, 0], [127, 0], [254, 0], 
    #             [0, 127], [127, 127], [254, 127]]
    goal_list = [[0, 0], [128, 0], [256, 0],
                [0, 128], [128, 128], [256, 128]]
    # white = balls[0]
    # ball_list = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    # for i in range(1, len(balls)):
    #     if balls[i][0] > 0 and balls[i][1] > 0:
    #         ball_list[i-1] = balls[i]
    if order == 1:
        target_index = [1, 3]
    elif order == 2:
        target_index = [2, 4]
    for i in range(len(target_index)):
        if balls[target_index[i]][0] < 0:
            target_index[i] = 0
    if target_index == [0, 0]:
        target_index = [5]
    print('target :', target_index)

    def find_hit_pos(hit_distance, hit_angle, hit_pos_list, obj_goal_distance, obj_goal_angle):
        for goal in goal_list:
            for target in target_index:
                if target == 0:
                    continue
                distance = math.sqrt((balls[target][0]-balls[0][0])**2 + (balls[target][1]-balls[0][1])**2)
                # 접점 찾기
                x = goal[0] - balls[target][0]
                y = goal[1] - balls[target][1]
                r = math.sqrt(x**2 + y**2)
                # if y == 0:
                #     if x > 0:
                #         radian = math.pi / 2
                #     elif x < 0:
                #         radian = (math.pi / 2)*3
                # elif y < 0:
                #     radian = math.atan(x/y) + math.pi
                # else:
                #     radian = math.atan(x/y)
                # theta = math.degrees(radian) % 360
                # if (goal == [127, 127] and (45 <= theta <= 315) or 
                #     goal == [127, 0] and (theta <= 135 or theta >= 225)):
                #     continue

                if x == 0:
                    if y > 0:
                        radian = math.pi / 2
                    elif y < 0:
                        radian = (math.pi / 2)*3
                elif x < 0:
                    radian = math.atan(y/x) + math.pi
                else:
                    radian = math.atan(y/x)
                theta = math.degrees(radian)
                if (
                    (goal == [127, 127] and not(45 <= theta <= 125)) or 
                    (goal == [127, 0] and not(225 <= theta <= 315))
                    ):
                    continue

                # print(x, y, r, theta)
                hit_pos = [balls[target][0] - 5.73*math.cos(radian), 
                           balls[target][1] - 5.73*math.sin(radian)]
                # 흰구를 접점으로 보낼 각도과 거리
                x0 = hit_pos[0] - balls[0][0]
                y0 = hit_pos[1] - balls[0][1]
                r0 = math.sqrt(x0**2 + y0**2)
                if r0 >= math.sqrt(distance**2 - 5.73**2):
                    continue
                if x0 == 0:
                    if y0 > 0:
                        hit_radian = math.pi / 2
                    elif y0 < 0:
                        hit_radian = (math.pi / 2)*3
                elif x0 < 0:
                    hit_radian = math.atan(y0/x0) + math.pi
                else:
                    hit_radian = math.atan(y0/x0)
                print('goal, hit_pos, hit_angle, theta :', goal, hit_pos, math.degrees(hit_radian), theta)
                hit_pos_list.append(hit_pos)
                hit_distance.append(r0)
                hit_angle.append(math.degrees(hit_radian))
                obj_goal_distance.append(r)
                obj_goal_angle.append(theta)


    def escaped_ball(hit_pos_list):
        # hit_pos  접점이랑 쿠션 
        # 내공 위치 x = balls[target][0]  y =  balls[target][1]
        r = 5.73
        notmyball = []
        for i in [1,2,3,4,5]:
            if i not in target_index:
                notmyball.append( (balls[i][0],balls[i][1])  )
        # notmyball = [(balls[2][0],balls[2][1]),(balls[4][0],balls[4][1])]
        
        for pos_num in range(len(hit_pos_list)):
            pos_i, pos_j = hit_pos_list[pos_num]

            # 상대방 ball 모두 확인
            for ball_num in range(len(notmyball)):
                nmb_i, nmb_j = notmyball[ball_num]

                area = abs((pos_i - nmb_i) * (balls[0][1] - nmb_j) - (pos_j - nmb_j) * (balls[0][0] - nmb_i))
                AB = ((pos_i - balls[0][0]) ** 2 + (pos_j - balls[0][1]) ** 2) ** 0.5
                distance = area / AB

                if distance < r:
                    hit_pos_list[pos_num] = 0 # 해당 좌표 는 0으로 바꿔주기

# x1y1 과 x2y2 직선에서 a,b 의 거리가 r 보다 큰지 구하는 식  
# def cal_dist(x1, y1, x2, y2, a, b):
#     area = abs((x1-a) * (y2-b) - (y1-b) * (x2 - a))
#     AB = ((x1-x2)**2 + (y1-y2)**2) **0.5
#     distance = area/AB
#     return distance
    
#     # pos_i pos_j / balls[target][0] balls[target][1]  는 pos 와 ball[][],   a,b = nmb 


    def find_cushion_pos(hit_pos_list_2, obj_goal_distance, hit_pos_list_cushion, hit_distance_cushion, hit_angle_cushion, obj_goal_distance_cushion):
        
        for k in range(len(hit_pos_list_2)):
            print(hit_pos_list_2[k])
            wall = [0, 0, 127, 254]     # 하 좌 상 우
            wall_distance = []
            for i in range(4):
                if i % 2 == 0:
                    wall_distance.append([abs(balls[0][1] - wall[i]) + abs(hit_pos_list_2[k][1] - wall[i]), i])
                else:
                    wall_distance.append([abs(balls[0][0] - wall[i]) + abs(hit_pos_list_2[k][0] - wall[i]), i])
            wall_distance.sort(key=lambda x: x[0])
            if wall_distance[0][1] == 0:
                # hit_pos_list_2[k][1] = 5.73 - hit_pos_list_2[k][1]
                hit_pos_list_2[k][1] = hit_pos_list_2[k][1]
            elif wall_distance[0][1] == 1:
                # hit_pos_list_2[k][0] = 5.73 - hit_pos_list_2[k][0]
                hit_pos_list_2[k][0] = hit_pos_list_2[k][0]
            elif wall_distance[0][1] == 2:
                # hit_pos_list_2[k][1] += 2 * (127-2.865 - hit_pos_list_2[k][1])
                hit_pos_list_2[k][1] += 2 * (127 - hit_pos_list_2[k][1])
            elif wall_distance[0][1] == 3:
                # hit_pos_list_2[k][0] += 2 * (254-2.865 - hit_pos_list_2[k][0])
                hit_pos_list_2[k][0] += 2 * (254-2.865 - hit_pos_list_2[k][0])

            x0 = hit_pos_list_2[k][0] - balls[0][0]
            y0 = hit_pos_list_2[k][1] - balls[0][1]
            r0 = math.sqrt(x0 ** 2 + y0 ** 2)
            if r0 >= math.sqrt(distance ** 2 - 5.73 ** 2):
                continue
            if x0 == 0:
                if y0 > 0:
                    hit_radian = math.pi / 2
                elif y0 < 0:
                    hit_radian = (math.pi / 2) * 3
            elif x0 < 0:
                hit_radian = math.atan(y0 / x0) + math.pi
            else:
                hit_radian = math.atan(y0 / x0)
            hit_pos_list_cushion.append(hit_pos_list_2[k])
            hit_distance_cushion.append(r0)
            hit_angle_cushion.append(math.degrees(hit_radian))
            obj_goal_distance_cushion.append(obj_goal_distance[k])


    hit_pos_list = []
    hit_distance = []
    hit_angle = []
    obj_goal_distance = []
    obj_goal_angle = []
    find_hit_pos(hit_distance, hit_angle, hit_pos_list, obj_goal_distance, obj_goal_angle)
    print(hit_pos_list, hit_distance, hit_angle)

    hit_pos_list_cushion = []
    hit_distance_cushion = []
    hit_angle_cushion = []
    obj_goal_distance_cushion = []
    # find_cushion_pos(hit_pos_list, obj_goal_distance, hit_pos_list_cushion, hit_distance_cushion, hit_angle_cushion, obj_goal_distance_cushion)
    escaped_ball(hit_pos_list)

    min_distance = math.sqrt((254-5.73)**2 + (127-5.73)**2)
    cnt = 0
    for i in range(len(hit_pos_list)):
        if hit_pos_list[i] == 0 and cnt != len(hit_pos_list):
        # if hit_pos_list[i] == 0:
            cnt += 1
            continue
        if min_distance > hit_distance[i] + obj_goal_distance[i]:
            min_distance = hit_distance[i] + obj_goal_distance[i]
            temp_angle = hit_angle[i] - obj_goal_angle[i]
            print(hit_angle[i])
            angle = (90 - hit_angle[i]) % 360
    # if cnt == len(hit_pos_list):
    #     for i in range(len(hit_pos_list_cushion)):
    #         if min_distance > hit_distance_cushion[i] + obj_goal_distance_cushion[i]:
    #             min_distance = hit_distance_cushion[i] + obj_goal_distance_cushion[i]
    #             print(hit_angle_cushion[i])
    #             angle = (90 - hit_angle_cushion[i]) % 360
    
    distance = min_distance
    power = distance * 0.2
    if power > 100:
        power = 100
    elif power < 20:
        power = 20

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')