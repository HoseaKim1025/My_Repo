############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def get_final_position(N, matrix, move_list):
    
    # 현재 위치 탐색
    # N*N 행렬 내에서 1이 존재하는 좌표를 curr에 리스트로 저장
    # 현재 좌표를 찾으면 모든 반복문을 중단하기 위해 flag 사용
    flag = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                curr = [i, j]
                flag == 1
                break
        if flag == 1:
            break

    # M에 따른 상하좌우 좌표 이동
    for M in move_list:
        if M == 0:
            curr[0] -= 1

        elif M == 1:
            curr[0] += 1

        elif M == 2:
            curr[1] -= 1

        elif M == 3:
            curr[1] += 1

        # 좌표 이동 중 N*N 범위 밖으로 나가면 None 반환
        if not(0 <= curr[0] <= N-1 and 0 <= curr[1] <= N-1):
            return

    # 모두 이동한 후 현재 좌표 반환
    return curr


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################