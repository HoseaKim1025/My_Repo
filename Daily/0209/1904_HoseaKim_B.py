def tile(n):
    # cnt = 2
    # ans = [0] * (n+1)
    # ans[0] = 1
    # ans[1] = 1
    # while cnt <= n:
    #     ans[cnt] += ans[cnt-1] + ans[cnt-2]
    #     cnt += 1
    
    # return ans[n]

    cnt = 2
    pre_0 = 1
    pre_1 = 1
    ans = 1
    temp = 0
    while cnt <= n:
        temp = (ans + pre_1) % 15746
        pre_0, pre_1 = pre_1, ans
        ans = temp
        cnt += 1
    
    return ans


n = int(input())
print(tile(n))