# while_login_retry_way1
password = 'A12345' #預設密碼
user = input('請輸入密碼：')
n = 2 #剩餘可登入次數
while user != password and n > 0:
	print('密碼錯誤！還有', n, '次機會')
	user = input('請輸入密碼：')
	n -= 1
if user == password:
	print('登入成功！')
else:
	print('密碼連續錯誤3次，請稍後再試！')