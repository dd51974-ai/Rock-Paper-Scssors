import random

def get_guess():
    return int(input("好きな数字を入れて下さい: "))

def check_guess(answer, guess): # match or unmatch
    if guess == answer:
        return "正解！"
    elif guess < 1 or guess > 10:
        return "数字は1〜10までです"
    elif guess < answer:
        return "惜しい！大きいです！"
    else:
        return "惜しい！小さいです！"

def play_game():
    answer = random.randit(1, 10)
    count = 1
    while count <= 3:
        guess = get_guess()
