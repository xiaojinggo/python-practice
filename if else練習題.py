age = int(input("請問你今年幾歲："))

if age < 0:
    print("年齡輸入錯誤")

else:
    if age < 6:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 150
    elif age <= 64:
        ticket_price = 300
    else:
        ticket_price = 200
    
    print(f"您的票價為{ticket_price}元")