in_str = input()

old_str = ''
new_str = ''

for i in in_str:
    if i == 'U' or i == 'C' or i == 'P':
        old_str += i

if 'UCPC' in old_str:
    print('I love UCPC')
elif set('UCPC') != set(old_str):
    print('I hate UCPC')

else:
    pre = 0
    try:
        index_1st_u = old_str.index('U')
    except ValueError:
        print('I hate UCPC')
    for j in old_str[index_1st_u:]:
        if j == 'U' and pre != 0:
            continue
        elif j == 'C' and pre != 'U' and pre != 'P':
            continue
        elif j == 'P' and pre != 'C':
            continue

        new_str += j
        pre = j

    if 'UCPC' in new_str:
        print('I love UCPC')
    else:
        print('I hate UCPC')