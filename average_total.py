numbers = [] # Charge number
while True:
    input_number = input("数を入力して下さい(終了はdone): ") #文字列で受け取る
    if input_number == "done":
        if len(numbers) == 0:
            print("数が入力されてません")
        else:# 合計・平均の処理
            total_amount = sum(numbers)
            average_amount = sum(numbers) / len(numbers)
            print("合計: ", total_amount)
            print("平均: ", average_amount)
            break
    elif input_number.isnumeric(): # 数字かどうか判定
        numbers.append(int(input_number)) #数値に変換
    else:
        print("数字を入力して下さい")