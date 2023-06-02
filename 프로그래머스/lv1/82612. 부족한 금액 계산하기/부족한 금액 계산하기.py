def solution(price, money, count):
    pay = 0
    for i in range(1, count+1): # 1부터 5까지
        pay += (price * i)  # (3*1) + (3*2) + (3*3) + (3*4)
    if money < pay: # 20 < 30 
        return pay - money # 30 - 20 = 10 
    else:
        return 0