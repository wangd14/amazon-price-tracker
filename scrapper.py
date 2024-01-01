from bs4 import BeautifulSoup
import requests
import time

def price_check(links, originalPrices):
    #Get page html
    for index, link in enumerate(links):
        job_page = requests.get(link).text
        soup = BeautifulSoup(job_page, 'lxml')

        #Product Information
        product_name = soup.find('span', class_ = 'a-size-large product-title-word-break').text.strip()
        price = soup.find('span', class_='a-offscreen').text

        #Prints it out
        print(f'{product_name}\n Price: {price} \n {link}')


        price = soup.find('span', class_='a-offscreen').text
        if(originalPrices[index] > float(price[1:].strip())):
            print('Price dropped')

if __name__ == '__main__':
    #Change inputs here
    links = ['https://www.amazon.com/A315-24P-R7VH-Display-Quad-Core-Processor-Graphics/dp/B0BS4BP8FB/ref=sr_1_3?crid=366I9FOHLRTUY&keywords=laptop&qid=1704067439&sprefix=laptop%2Caps%2C150&sr=8-3&th=1',
             'https://www.amazon.com/Chesapeake-Bay-Candle-Serenity-Lavender/dp/B07GH691SQ/ref=sr_1_6?crid=VETMUB53OZJV&keywords=candle&qid=1704069033&sprefix=%2Caps%2C135&sr=8-6&th=1']
    originalPrices = [259.00, 12.49] #Input the original price of the item in this array corresponding to the index in the links
    delay = 24 #in hours

    while True:
        price_check(links, originalPrices)
        time.sleep(60*60*delay)
