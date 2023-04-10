def find_nth_occurrence(s, char, n):
    i = -1
    for _ in range(n):
        i = s.find(char, i + 1)
        if i == -1:
            return -1
    return i


# print(find_nth_occurrence("hello", "l", 2))  # Output: 3


while True:
    try:
        s = input()
        pos = find_nth_occurrence(s, '/', 3)
        file_name = s[pos:]
        url = 'https://10.0.62.21/source' + file_name
        print(url)
    except EOFError:
        break
