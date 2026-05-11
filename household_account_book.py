import json
money_list = {}

# Save
with open("money_list.json", "r") as f:
    money_list = json.load(f)

while True:
    print("1: 収入を追加")
    print("2: 支出を追加")
    print("3: 残高を確認")
    print("4: 履歴を表示")
    print("5: 終了")
    choices = input("選択して下さい: ")