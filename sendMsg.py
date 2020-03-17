import smtplib

smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
print(smtpObj.starttls())

smtpObj.login('sportshop174@inbox.ru','KSJdjak3j;kAJWfje')

smtpObj.sendmail('sportshop174@inbox.ru', 
		"anton16780hgh1anton@gmail.com", 
		"hello")
smtpObj.quit()
