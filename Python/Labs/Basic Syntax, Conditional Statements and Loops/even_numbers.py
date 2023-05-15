n = int(input())

even_counter = 0

for num in range (n):
    new_num = int(input())
    if new_num % 2 == 1:
        print(f"{new_num} is odd!")
        break
    else:
        even_counter += 1


if even_counter == n:
    print("All numbers are even.")