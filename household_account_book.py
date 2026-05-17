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

    # Kind of income
    category_income = {
        "1": "収入",
        "2": "賞与",
        "3": "その他"
    }

    # Choice 1
    if choices == "1":
        choices_deposit = input("収入金額を記入して下さい: ")
        if choices_deposit == "":
            print("金額を入力して下さい")
            continue

        choices_type = input("種類を選んで下さい 1: 収入, 2: 賞与, 3: その他: ")
        category_name = category_income.get(choices_type, "不明")
        data = {
            "category": category_name
        }
        with open("total_money.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        choices_memo = input("メモを記入して下さい: ")
        # Calculation addtion
        total_money = [choices_deposit, choices_type, choices_memo]
        print("{:,}円入金しました！".format(int(choices_deposit)))
        if choices_type == "1":
            print(f"種類: {category_income[choices_type]}", "金額: {:,}円".format(int(choices_deposit)), f"メモ: {choices_memo}")
        elif choices_type == "2":
            print(f"種類: {category_income[choices_type]}", "金額: {:,}円".format(int(choices_deposit)), f"メモ: {choices_memo}")
        elif choices_type == "3":
            print(f"種類: {category_income[choices_type]}", "金額: {:,}円".format(int(choices_deposit)), f"メモ: {choices_memo}")
        else:
            print("金額を入力して下さい")
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
    if choices == "5":
        print("終了します")
        break