import random

random_number = random.randint(1, 10) # Decide number something
game_count = 0 # Counter is 0

# Start loop
while True:
    games = int(input("数を入力して下さい: "))
    game_count += 1
    if game_count == 1 and games == random_number:
        print("素晴らしい！一発で決めましたね！")
        break
    elif games > random_number:
        print("惜しい！小さいです")
    elif games < random_number:
        print("惜しい！大きいです")
    else:
        print("正解！", game_count, "回かかりました")
        break

    if game_count == 10:
        print("残念！ゲームオーバーです・・・")
        break
