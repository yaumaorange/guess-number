import random

number = random.randint(1, 100)

while True:
	guess = int(input('請猜一個數字:'))
	if guess == number:
		print('恭喜答對~!')
		break
	elif guess > number:
		print("再小一點")
	else:
		print('再大一點')
		
	