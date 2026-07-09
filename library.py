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
        books = data.get("books", [])

book = {

    "返す本の番号": books,
    "本の名前": "",
    "借りる人の名前": None,
    "貸出": False,
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
            # 空欄チェックを機能させる(Avoid to empty registration book title)
            if book_title_register == "":
                print("記入をお願いします")
                continue
            else:
                books.append({"借りる本の番号": len(books) + 1, "返す本の番号": len(books) + 1, "本の名前": book_title_register, "貸出": False, "完了": False})
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

            print("この番号は存在します")

            # 貸出をする
            # 本が未貸出ならここで貸出処理
            if found_book["貸出"] == False:
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
    # 要修正
    elif choices == "3":
        return_book = input("借りてる本の番号を入力して下さい: ")
        find_out = None
        for a in books:
            if str(a["返す本の番号"]) == return_book:
                find_out = a
                break
            # ここで終わり。「見つからなかった時の処理」はループの外に出す

        # find_outで見つけた該当の本をその後の処理に使う
        if find_out is None:
            print("番号が見つかりません")
            continue
        if find_out["貸出"] == False:
            print("この本はまだ借りられてません")
            continue
        find_out["貸出"] = False
        find_out["完了"] = True
        # 返却したので借りてる人をリセット(任意)
        find_out["借りる人の名前"] = None
        print("返却完了")
        save_data()

    # 一覧表示
    elif choices == "4":
        if not books:
            print("リストがありません")
        else:
            print("一覧表示")
            for i, record in enumerate(books, 1):
                mark = "✅" if record["完了"] else record[" "] == " "
                print(f"[{mark} ]{i}, {record['本の名前']}")

    elif choices == "5":
        print("終了します")
        break