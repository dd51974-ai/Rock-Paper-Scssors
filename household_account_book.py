import json
import os
total_money = []
money_list = {}

if os.path.exists("money_list.json"):
    # Read
    with open("money_list.json", "r") as f:
        money_list = json.load(f)

while True:
    print("1: 収入を追加")
    print("2: 支出を追加")
    print("3: 残高を確認")
    print("4: 履歴を表示")
    print("5: 終了")
    choices = input("選択して下さい: ")

    # Choice 1
    if choices == "1":
        choices_deposit = input("収入金額を記入して下さい")
        choices_type = input("種類を選んで下さい 1: 収入, 2: 支出")
        choices_memo = input("メモを記入して下さい")
        if choices_type == "1":
            print(f"種類: {choices_type}",  f"金額: {choices_deposit}",  f"メモ: {choices_memo}")
        # Calculation addtion
        total_money = choices_deposit
        print(f"{total_money}円入金しました！")
        # Save
        with open("total_money.json", "w") as f:
            json.dump(total_money, f)

    # Choice 2 withdrawal
    if choices == "2":
        choices_withdrow = input("支出金額を記入して下さい")
        withcash = total_money - choices_withdrow
        print
    # Choice 3 to balance
    if choices == '3':
        choices_balance = total_money
        if choices_balance in money_list:
            money_list
            print(total_money, ":", money_list[total_money])
    # Choice 4 resume
    # Choice 5 to end