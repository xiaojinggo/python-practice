password = "abc123"
count = 0
success = False

while count < 3 and not success:
    user_input = input("請輸入密碼：")
    count += 1

    if user_input == password:
        success = True
    else:
        print(f"密碼錯誤，還剩 {3 - count} 次機會")

if success:
    print("登入成功")
else:
    print("帳號已鎖定")