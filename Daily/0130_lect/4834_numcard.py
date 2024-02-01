T = int(input())
for case in range(1, T+1):
    n = int(input())    # 카드의 장수
    card_list = list(map(int, input()))

    cnt = [0] * 10  # 0~9
    for card in card_list:
        cnt[card] += 1

    card_num = 0
    max_cnt = 0
    for i in cnt:
        if max_cnt <= i:
            max_cnt = i
            max_card = card_num
        card_num += 1
    print(f'#{case} {max_card} {max_cnt}')
