num = float(input())

if num > 0:
    if 0 < abs(num) < 1:
        print("small positive")
    elif abs(num) > 1000000:
        print("large positive")
    else:
        print("positive")
elif num < 0:
    if 0 < abs(num) < 1:
        print("small negative")
    elif abs(num) > 1000000:
        print("large negative")
    else:
        print("negative")
else:
    print("zero")