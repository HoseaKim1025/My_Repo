############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def tidy_up_company(email_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    # email_list를 set로 변환해 중복 제거
    email_set = set(email_list)

    # email_set의 각 요소를 key로 하고 value는 모두 0인 new_dict 생성
    new_dict = {}
    for i in email_set:
        new_dict[i] = 0

    # new_dict의 key와 일치하는 email 이름이 email_list에서 나올 때마다
    # 해당 value를 +1하여 각 email 이름이 몇 개 있는지 카운트
    for j in email_list:
        new_dict[j] += 1
            
    return new_dict


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
email_list1 = ['Koogle', 'Koogle', 'Maver']
print(tidy_up_company(email_list1))   # {'Koogle': 2, 'Maver': 1}

email_list2 = [
    'Koogle', 'Koogle', 'JCloud', 'Koogle', 'GaKao', 
    'School', 'Koogle', 'Maver', 'GaKao', 'Maver', 
    'Koogle', 'GaKao', 'School', 'GaKao', 'JCloud', 
    'School', 'GaKao', 'GaKao', 'Maver', 'Koogle'
]
print(tidy_up_company(email_list2))
# {'Koogle': 6, 'JCloud': 2, 'GaKao': 6, 'School': 3, 'Maver': 3}
#####################################################
