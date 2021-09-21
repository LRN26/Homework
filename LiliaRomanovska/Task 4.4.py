def split_by_index(s, indexes):
    s_splited = []
    s_counter = 0

    for i in indexes:
        if i <= 0:
            continue
        s_splited.append(s[s_counter:i])
        s_counter = i

        if i > len(s):
            break

        if i < len(s):
            s_splited.append(s[s_counter:])

    return s_splited

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
