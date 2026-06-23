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