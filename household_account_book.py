import json
import os
# Resume list
total_money = []
# Balance
money_list = 0

# Create def save_data():
def save_data():
    with open("money_list.json", "w", encoding="utf-8") as f:
        json.dump({"total_money": total_money, "money_list": money_list}, f, ensure_ascii=False, indent=2)

# save_data()の中に読み込みを入れるのはNG
if os.path.exists("money_list.json"):
    # Read
    with open("money_list.json", "r", encoding="utf-8") as f:
        data = json.load(f) #まずdataに読み込む
        total_money = data.get("total_money", [])
        money_list = data.get("money_list", 0)

# Create to choice category income
category_income = {
    "1": "収入",
    "2": "賞与",
    "3": "その他"
}
# Create to choice category expense
category_expense = {"1": "食費", "2": "交通費", "3": "その他"}
while True:
    print("1: 収入を追加")
    print("2: 支出を追加")
    print("3: 残高を確認")
    print("4: 履歴を表示")
    print("5: 終了")
    choices = input("選択して下さい: ")

    # Choice 1 income
    if choices == "1":
        while True:
            choices_deposit = input("収入金額を記入して下さい: ")
            if choices_deposit == "" or not choices_deposit.isdigit(): #数字のみで構成されてるか
                print("正しい金額を入力して下さい")
                continue
            elif int(choices_deposit > "0"):
                break


        # 種類の入力を内側のループで繰り返す
        while True:
            choices_type = input("種類を選んで下さい 1: 収入, 2: 賞与, 3: その他: ")
            if choices_type in ("1", "2", "3"):
                break
            else:
                print("指定された数字を入力して下さい")
                continue
        category_name = category_income.get(choices_type, "不明")
        data = {
            "category": category_name
        }

        choices_memo = input("メモを記入して下さい: ")
        # Calculation addtion

        # Add resume
        amount = int(choices_deposit)
        money_list += amount # Add balance

        # Add dictionary methods in resume list 履歴リストに辞書形式で追加＊重要な修正
        total_money.append({
            "種別": "収入",
            "カテゴリ": category_name,
            "金額": amount,
            "メモ": choices_memo
        })

        print("{:,}円入金しました！".format(int(choices_deposit)))
        if choices_type == "1":
            print(f"種類: {category_income[choices_type]}", "金額: {:,}円".format(int(choices_deposit)), f"メモ: {choices_memo}")
        elif choices_type == "2":
            print(f"種類: {category_income[choices_type]}", "金額: {:,}円".format(int(choices_deposit)), f"メモ: {choices_memo}")
        elif choices_type == "3":
            print(f"種類: {category_income[choices_type]}", "金額: {:,}円".format(int(choices_deposit)), f"メモ: {choices_memo}")
        else:
            print("金額を入力して下さい")
        # Save json 2
        save_data()
    # Choice 2 withdrawal
    elif choices == "2":
        while True:
            choices_withdrawal = input("支出金額を記入して下さい")
            if choices_withdrawal == "" or not choices_withdrawal.isdigit():
                print("金額を入力し直して下さい")
                continue
            elif int(choices_withdrawal) > 0:
                break

        while True:
            choices_type = input("種類を選んでください 1: 食費, 2: 交通費, 3: その他 ")
            if choices_type in ("1", "2", "3"):
                break
            else:
                print("指定された数字を選択して下さい")
                continue
        category_name = category_expense.get(choices_type, "不明")
        choices_memo = input("メモを記入して下さい: ")
        amount = int(choices_withdrawal)
        money_list -= amount
        # Add dictionary methods in resume list 履歴リストに辞書形式で追加＊重要な修正
        total_money.append({
            "種別": "支出",
            "カテゴリ": category_name,
            "金額": amount,
            "メモ": choices_memo
        })

        print("{:,}円出金しました!".format(int(choices_withdrawal)))
        save_data()

    # Choice 3 to balance
    elif choices == '3':
        print("現在の残高{:,}円".format(money_list))
    # Choice 4 resume
    elif choices == '4':
        if not total_money:
            print("履歴がありません")
        else:
            for i, record in enumerate(total_money, 1):
                print(f"{i}. {record['種別']} / {record['カテゴリ']} / {record['金額']:,}円 / {record['メモ']}")

    # Choice 5 to end
    elif choices == "5":
        print("終了します")
        break