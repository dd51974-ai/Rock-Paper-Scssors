import json
import os
books = []
print(len(books))

# Create def save_data():
def save_data():
    with open("library_books_list.json", "w", encoding="utf-8") as f:
        json.dump({"books": books}, f, ensure_ascii=False, indent=1)

# Roading
if os.path.exists("todo_list.json"):
    with open("library_books_list.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        tasks = data.get("books", [])

book = {
    "借りる本の番号": books,
    "本の名前": "",
    "借りる人の名前": "",
    "返却": False
}

while True:
    print("1: 本を新規登録")
    print("2: 本を借りる")
    print("3: 本を返す")
    print("4: 一覧表示")
    print("5: 終了")
    choices = input("選択して下さい")

    if choices == "1":
        while True:
            new_register = input("本を新規登録して下さい")
            books.append({"借りる本の番号": books, "本の名前": len(""), "借りる人の名前": len(""), "完了": False})
            print(len(books))
            if books == "":
                print("記入をお願いします")
                continue
            else:
                save_data()
                break

    elif choices == "2":
        # 本を借りる
        while True:
            check_number = input("本の登録番号を入力して下さい")
            if books == check_number:
                print("この番号は存在します")
                if books == True:
                    print("この本は貸し出しできます")
                    # 貸出人の名前
                    borrower = input("お名前を記入して下さい: ")
                    # 借りる本の名前
                    rental_book = input("本の名前を記入して下さい")
                    books.append({"借りる人の名前": borrower, "本の名前": rental_book, "貸出": False})
                    print(len(books))
                    print("貸出完了")
                    save_data()

            else:
                print("番号が見つかりません")
                continue