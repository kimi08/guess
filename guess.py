import random
count = 0
start = input('請輸入開始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
while True:
    count += 1 #count = 1 + count 
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜中了')
        print('這是你猜的第', count , '次')
        break
    elif num < r:
        print('比答案小')
    elif num > r:
        print('比答案大')
    print('這是你猜的第', count , '次')