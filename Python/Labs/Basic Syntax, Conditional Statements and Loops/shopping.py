budget = int(input())

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    price = int(command)
    if budget < price:
        print("You went in overdraft!")
        break
    budget -= price

