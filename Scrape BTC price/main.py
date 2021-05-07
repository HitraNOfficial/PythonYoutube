from bs4 import BeautifulSoup
import requests
import time
from playsound import playsound

def scrape():
    url = 'https://coinmarketcap.com/currencies/bitcoin/'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    current_price_element = soup.body.find(class_='priceValue___11gHJ')
    return current_price_element.text.replace('$', '').replace(',', '')

target_price = 60000
while True:
    time.sleep(5)
    current_price = float(scrape())

    if target_price >= current_price:
        playsound('audio.wav')
