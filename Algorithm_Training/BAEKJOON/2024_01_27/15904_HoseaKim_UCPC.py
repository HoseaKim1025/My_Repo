in_str = input()

old_str = ''
new_str = ''
for i in in_str:
    if i == 'U' or i == 'C' or i == 'P':
        old_str += i
if 'UCPC' in old_str:
        print('I love UCPC')
else:
    pre = 0
    index_1st_u = old_str.index('U')
    for j in old_str[index_1st_u:]:
        if pre == 0 and j == 'U':
            new_str += j
            pre = j
        elif j == 'C' and (pre == 'U' or pre == 'P'):
            new_str += j
            pre = j
        elif j == 'P' and pre == 'C':
            new_str += j
            pre = j
        pre = None
    if 'UCPC' in new_str:
        print('I love UCPC')
    else:
        print('I hate UCPC')