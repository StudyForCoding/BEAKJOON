while True:
    input_str = input().rstrip()
    if input_str == "0 0 0":
        break
    side = list(map(int, input_str.split()))
    side.sort()
    one = (side[0]**2) + (side[1]**2)
    two = side[2]**2
    if one == two:
        print("right")
    else:
        print("wrong")