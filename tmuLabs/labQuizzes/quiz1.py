def tuesday8am(a, b, c):
    result = -999999999999
    for i in [a, b, c]:
        if result < i:
            result = i
    return f'Output: {result} \n There is no standout number' if a == b == c else f' Output: {result}'


# print(tuesday8am(int(input()), int(input()), int(input())))
