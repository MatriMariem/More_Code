def different_occurences(s):
    """ this function takes a string and returns the minimum number of letters that should be deleted
    in order to get a string in which all occurences of letters are not the same """
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)
    l = [v for v in d.values()]
    print(l)
    l = sorted(l)[::-1]
    print(l)
    c = 0
    for i in range(len(l) - 1):
        while l[i] != 0 and l[i] in s[:i] + s[i+1:]:
            l[i] -= 1
            c += 1
    return c
