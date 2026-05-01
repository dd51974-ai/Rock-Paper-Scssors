import random

random_number = random.randint(1, 10) # Decide number something
game_count = 0 # Counter is 0

# Start loop
while True:
    games = int(input("数を入力して下さい: "))
    game_count += 1
    if games > random_number:
        print("小さい")
    elif games < random_number:
        print("大きい")
    elif game_count == 1 and games == random_number:
        print("素晴らしい！一発で決めましたね！")
        break
    elif game_count >= 2:
        print("残念！ゲームオーバーです・・・")
        break
    else:
        print("正解！", game_count, "回かかりました")
        break
