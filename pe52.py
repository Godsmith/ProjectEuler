def up_to_6x_contains_same_digits(i: int):
    strings = [str(i*j) for j in range(1,7)]
    for s in strings[1:]:
        for d in strings[0]:
            if not d in s:
                return False
            s = s.replace(d, '', 1)
        if s != '':
            return False
    return True

i = 0
while True:
    i += 1
    if up_to_6x_contains_same_digits(i):
        print(i)
        exit()