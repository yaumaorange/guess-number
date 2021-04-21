import random

start = int(input('最小數字:'))
end = int(input('最大數字:'))
number = random.randint(start, end)
i = 0

while True:
	i += 1 #i = i + 1
	guess = int(input('請猜一個數字:'))
	if guess == number:
		print('恭喜答對~!')
		print('你總共猜了', i, '次')
		break
	elif guess > number:
		print("再小一點")
	else:
		print('再大一點')

		
	