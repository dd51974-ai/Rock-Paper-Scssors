import json
import os
books = []
print(len(books))

# Create def save_data():
def save_data():
    with open("library_books_list.json", "w", encoding="utf-8") as f:
        json.dump({"books": books}, f, ensure_ascii=False, indent=1)

# Roading
if os.path.exists("library_books_list.json"):
    with open("library_books_list.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        tasks = data.get("books", [])

book = {
    "借りる本の番号": books,
    "本の名前": "",
    "借りる人の名前": None,
    "返却": False
}

while True:
    print("1: 本を新規登録")
    print("2: 本を借りる")
    print("3: 本を返す")
    print("4: 一覧表示")
    print("5: 終了")
    choices = input("選択して下さい: ")

    if choices == "1":
        while True:
            print("本の新規登録をお願いします: ")
            book_title_register = input("本のタイトルを入力して下さい: ")

            books.append({"借りる本の番号": len(books) + 1, "本の名前": book_title_register, "完了": False})
            print(len(books))
            if books == "":
                print("記入をお願いします")
                continue
            else:
                save_data()
                print("登録しました")
                break

    elif choices == "2":
        # 本を借りる
        while True:
            check_number = input("本の登録番号を入力して下さい: ")
            found_book = None
            # 番号を見つけるためのfor文
            for b in books:
                if str(b["借りる本の番号"]) == check_number:
                    found_book = b
                    break
            if found_book is None:
                print("番号が見つかりません")
                break
            elif found_book is True:
                print("この番号は存在します")
                continue
            # 貸出をする
            elif found_book["完了"] is False:
                print("この本は貸出できます")
                # 貸出人の名前
                borrower = input("お名前を記入して下さい: ")
                # 既存の本の情報を更新する（新しい要素を追加しない）
                found_book["借りる人の名前"] = borrower
                found_book["貸出"] = True
                print("貸出完了")
                save_data()
                break
            else:
                print("この本は現在貸出中です")
                break

    # 借りた本を返却
    elif choices == "3":
        return_book = int(input("借りてる本の番号を入力して下さい: "))
        if 0 < return_book < books:
            data = json.loads("library_books_list.json")
            return_book = False
            print("返却完了")
            save_data()
            break
        else:
            print("番号が存在しません")
            continue

    # 一覧表示
    elif choices == "4":
        if not books:
            print("リストがありません")
        else:
            print("一覧表示")
            for i, record in enumerate(books, 1):
                mark = "✅" if record["完了"] else " "
                print(f"[{mark} ]{i}, {record["本の名前"]}")

    elif choices == "5":
        print("終了します")
        break