
while True:
    pass_word = input("パスワードを入力して下さい: ")
    if len(pass_word) >= 8 and any(c.isdigit() for c in pass_word) and any(c.isupper() for c in pass_word):
        print("パスワードが設定されました!")
        break
    elif len(pass_word) < 8:
        print("8文字以上にして下さい")
    elif not any(c.isdigit() for c in pass_word):
        print("数字を入れて下さい")
    elif not any(c.isupper() for c in pass_word):
        print("英語の大文字を入れて下さい")
    else:
        print("パスワードを入力して下さい")

