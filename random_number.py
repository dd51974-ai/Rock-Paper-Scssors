import random

answer = random.randint(1,10)

guess = int(input("1~10の数字を入力してください: "))

if guess == answer:
    print("正解")
else:
    print("ハズレ！答えは", answer)