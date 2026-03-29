import random

answer = random.randint(1, 10)

for x in range(3):
    guess = int(input("好きな数字を入力して下さい: "))
    if answer == guess:
        print("正解!")
        break
    elif guess <= -1 or guess >= 11:
        print("数字は1~10までです")
    else:
        print("残念！正解は", answer)
