import random

answer = random.randint(1,10)
guess = int(input("好きな数字を入力して下さい: "))

if answer == guess:
    print("正解!")
elif guess > answer:
    print("数字は1~10までです")
else:
    print("残念！正解は", answer)