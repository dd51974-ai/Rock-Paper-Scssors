import random

answer = random.randint(1,20)

guess = int(input("1~10の数字を入力してください: "))

if guess == answer:
    print("正解")
elif guess > answer:
    print("数字を入力し直してください")
else:
    print("ハズレ！答えは", answer)