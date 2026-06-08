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
    todo_list = input("本日のすることを記入して下さい")