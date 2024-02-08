def valence(string):
    str_len = len(string)
    top = -1
    st = [0] * str_len
    couple = {')': '(', ']': '['}
    for i in range(str_len):
        if string[i] in couple.values():
            top += 1
            st[top] = string[i]
        elif string[i] in couple.keys():
            if couple.get(string[i]) == st[top]:
                st[top] = 0
                top -= 1
            else:
                return 'no'
    if st[0]:
        return 'no'
    else:
        return 'yes'


while True:
    in_str = input()
    if in_str == '.':
        break

    print(valence(in_str))
