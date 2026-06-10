import json
import os
# Todo list
tasks = []

# Create def save_data()
def save_data():
    with open("todo_list.json", "w", encoding="utf-8") as f:
        json.dump({"tasks": tasks}, f, ensure_ascii=False, indent=1)

# Roading
if os.path.exists("todo_list.json"):
    with open("todo_list.json", "r", encoding="uft-8") as f:
        data = json.load(f)
        tasks = data.get("tasks", [])

while True:
    print("1: タスクを追加")
    print("2: タスクを完了する")
    print("3: タスクを削除")
    print("4: タスク一覧を表示")
    print("5: 終了")

    if choices == "1":
        while True:
            todo_list = input("本日のすることを記入して下さい: ")
            if todo_list == "":
                print("記入をお願いします")
                continue
            else:
                save_data()
                break