import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Set URL you want to search
URL = 'https://www.amazon.co.uk/Nintendo-Switch-Neon-Red-blue/dp/B07W4CK8KR/ref=sr_1_4?crid=3VS40UOZSEXSM&dchild=1&keywords=nintendo+switch&qid=1613684389&sprefix=nitendo+sw%2Caps%2C158&sr=8-4'
#search for header user agent in google
headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
#gets the URL using PCs headers
page = requests.get(URL, headers=headers)


def check_price():

    #Creates soup
    soup = BeautifulSoup(page.content, 'html.parser')

    #1) Gets the title, dev tools, element get the ID
    title = soup.find(id="productTitle").get_text()
    #2)prints only the text/removes blanks
    # print(title.strip())


    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])
    print(converted_price)
    if converted_price > 250:
        send_email()
    


def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('moisesleetest@gmail.com','zizehjpeyvsytyoh')

    subject = 'Python Nintendo Switch Scraper'
    body = 'Check the amazon link https://www.amazon.co.uk/Nintendo-Switch-Neon-Red-blue/dp/B07W4CK8KR/ref=sr_1_4?crid=3VS40UOZSEXSM&dchild=1&keywords=nintendo+switch&qid=1613684389&sprefix=nitendo+sw%2Caps%2C158&sr=8-4'
    msg = f"Subject: {subject}\n\n{body}"

# (sender email, recipient email)
    server.sendmail(
    'moisesleetest@gmail.com',
    'moisesleetest@gmail.com',
    msg    

    )
    print('EMAIL SENT!')
    server.quit()


while(True):
    check_price()
    time.sleep(10)

#run code python3 scraper.py