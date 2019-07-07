import requests
from bs4 import BeautifulSoup
import smtplib
import time
#put url of the product you want
URL = 'https://www.amazon.in/Boat-BassHeads-900-Wired-Headphone/dp/B074ZF7PVZ/ref=sr_1_5?crid=IO1C10CTZXJT&keywords=boat+headphones&qid=1562476892&s=gateway&sprefix=boat%2Caps%2C340&sr=8-5'

headers = {"User-Aent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
def check_price():

	page = requests.get(URL,headers = headers)

	sp = BeautifulSoup(page.content,'html.parser')
	title = sp.find(id = 'productTitle').get_text()
	price = sp.find(id= 'priceblock_ourprice').get_text()
	intprice = int(price[2:5])

	if intprice <= 800 :
		send_mail(intprice)

def send_mail(a) :
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('tokirmanva22@gmail.com','Enter your Password')
	subject = 'Product is Selling at your Price...Buy Fast at {} rs only!!'.format(a)
	body  = 'Check the Product Link \n https://www.amazon.in/Boat-BassHeads-900-Wired-Headphone/dp/B074ZF7PVZ/ref=sr_1_5?crid=IO1C10CTZXJT&keywords=boat+headphones&qid=1562476892&s=gateway&sprefix=boat%2Caps%2C340&sr=8-5'
	#msg = f'Subject: {subject} \n {body}'
	msg = "Subject:{} \n\n {}"
	server.sendmail('tokirmanva22@gmail.com','2017kucp1019@iiitkota.ac.in',msg.format(subject,body))
	print("Email has been Sent !!")
	server.quit()
while True :

	check_price()
	time.sleep(12*60*60)
