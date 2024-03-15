############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def find_solo(number_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # num_list로부터 num1을 인자로 받는다.
    # 같은 수가 발견되면 flag = 1, 발견되지 않으면 flag = 0이 되도록 한다.
    for num1 in number_list:
        flag = 0

        # num1이 있는 index 이후부터 num2를 인자로 받는다.
        for num2 in number_list[number_list.index(num1)+1:]:
            # 탐색 중 num1과 num2가 같은 경우가 발견되면 flag = 1이 되고
            # 발견되지 않으면 기존의 flag = 0이 그대로 뒤로 넘어간다.
            if num1 == num2:
                flag = 1
                break

        # 위 반복문에서 짝이 발견되지 않아 flag가 0으로 넘어오면 해당 숫자를 반환한다.
        if flag == 0:
            return num1
    
    # num_list의 각 num을 인자로 받아 해당 num을 하나 지운다.
    for num in number_list:
        number_list.remove(num)

        # num_list에 num이 하나 더 있다면 하나 더 지운다.
        if num in number_list:
            number_list.remove(num)

        # 없다면 짝이 없으므로 해당 num을 반환
        else:
            return num


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################