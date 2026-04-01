import random
import time

answer = random.randint(1, 10)
count_time = time
x = 1
while x <= 3:
    guess = int(input("好きな数字を入力して下さい: "))
    if guess <= -1 or guess >= 11:
        print("数字は1~10までです")
    if answer == guess:
        print("正解!")
        break
    elif guess > answer:
        print("惜しい！小さいです")
    else:
        print("惜しい！大きいです")

    x += 1
else:
    print("残念！ゲームオーバーです")