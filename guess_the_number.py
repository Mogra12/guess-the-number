import random


num = random.randint(0,10)
entry = int(input("> "))


def main():
    if entry == num:
        print("Correct")
    else:
        print("Wrong")

main()
