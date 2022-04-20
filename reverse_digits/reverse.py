def digitize(n):
    reversed_list = list(str(n))[::-1]
    return [int(item) for item in reversed_list]

print(digitize(348597))