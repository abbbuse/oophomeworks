def multiple(*args):
    multi = 1
    for num in args:
        multi = multi * num
    print(multi)

multiple(2, 3, 3)
multiple(2, 1)