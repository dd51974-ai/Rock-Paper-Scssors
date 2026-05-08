
while True:
    pass_word = input("パスワードを入力して下さい: ")
    errors = []
    if len(pass_word) >= 8 and any(c.isdigit() for c in pass_word) and any(c.isupper() for c in pass_word):
        print("⭕️パスワードが設定されました!")
        break
    if len(pass_word) < 8:
        print("8文字以上にして下さい")
    if not any(c.isdigit() for c in pass_word):
        errors.append("数字を入れて下さい")
    if not any(c.isupper() for c in pass_word):
        errors.append("英語の大文字を入れて下さい")
    if len(errors) == 0:
        print("パスワードが設定されました！")
        break
    else:
        for error in errors:
            print("❌", error)
