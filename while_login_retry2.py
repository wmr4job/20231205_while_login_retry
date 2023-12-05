# while_login_retry_way2
password = 'A12345' #預設密碼

n = 3 #剩餘可登入次數
while n > 0:
	user = input('請輸入密碼：')
	if user == password:
		print('登入成功！')
		break #跳出迴圈
	else:
		n -= 1
		print('密碼錯誤！還有', n, '次機會')
if n == 0:
	print('密碼連續錯誤3次，請稍後再試！')