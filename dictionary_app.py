import json
dictionary = {}

# Read
with open("dictionary.json", "r") as f:
    dictionary = json.load(f)


while True:
    print("1: 単語を登録")
    print("2: 単語を検索")
    print("3: 終了")
    choices = input("1~3を選択して下さい: ")

    if choices == "1":
        choices_word = input("単語を登録して下さい: ")
        choices_mean = input("意味を入力して下さい: ")
        dictionary[choices_word] = choices_mean
        print("登録しました!")

        # Save
        with open("dictionary.json", "w") as f:
            json.dump(dictionary, f)

    elif choices == "2":
        choices_2 = input("単語を検索して下さい: ")
        # 辞書に存在するか確認する
        if choices_2 in dictionary:
            dictionary
            print(choices_2, ":", dictionary[choices_2]) #その単語の意味だけ表示
        else:
            print("!単語が見つかりません!")
    elif choices == "3":
        print("終了します")
        break
