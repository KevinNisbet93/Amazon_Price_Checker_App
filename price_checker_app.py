import requests
from bs4 import BeautifulSoup
import smtplib
import time
from fake_useragent import UserAgent

ua = UserAgent()

URL = "https://www.amazon.co.uk/Bluetooth-Headphones-Canceling-Waterproof-compatible-Neuestes-Modell/dp/B086Q4XSLG" \
      "/ref=redir_mobile_desktop?ie=UTF8&aaxitk=Y2NLPywkfrCAHpE8B1CUZw&hsa_cr_id=3372427150602&ref_=sb_s_sparkle "

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.122 Safari/537.36"}


def check_price():

    # generate random header to avoid being blocked
    page = requests.get(URL, headers={'User-Agent': ua.random})
    soup = BeautifulSoup(page.text, 'lxml')

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])  # convert the price sting to a float and remove currency sign

    if converted_price < 25:
        send_email()
        quit()
    else:
        print("The price is still {}".format(price))


def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("kevinnisbet93@gmail.com", "clhwrliulfmqlppg")
    subject = "Price has been lowered"
    body = "Check the amazon link https://www.amazon.co.uk/Bluetooth-Headphones-Canceling-Waterproof-compatible" \
           "-Neuestes-Modell/dp/B086Q4XSLG/ref=redir_mobile_desktop?ie=UTF8&aaxitk=Y2NLPywkfrCAHpE8B1CUZw&hsa_cr_id" \
           "=3372427150602&ref_=sb_s_sparkle "
    msg = f"subject: {subject}\n\n {body}"
    server.sendmail("kevinnisbet93@gmail.com", "k3v_gers@hotmail.com", msg)
    print("Email has been sent")
    server.quit()


while True:
    check_price()
    time.sleep(43200)
