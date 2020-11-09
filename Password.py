password = 'abcd1234'
i = 3
while True:
	pwd = input('Password: ')
	if pwd == password:
		print('Password Correct!')
		break
	else:
		i = i - 1
		print('Wrong Password! ', i, 'Attemp Left')
		if i == 0:
			print('No attemp left')
			break
