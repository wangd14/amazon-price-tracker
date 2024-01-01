from bs4 import BeautifulSoup
import requests
import time

def price_check(link, delay):
    #Get page html
    job_page = requests.get(link).text
    soup = BeautifulSoup(job_page, 'lxml')

    #Product Information
    product_name = soup.find('span', class_ = 'a-size-large product-title-word-break').text.strip()
    price = soup.find('span', class_='a-offscreen').text

    #Prints it out
    print(f'{product_name}\n Price: {price} \n {link}')

    originalPrice = price
    
    while True:
        price = soup.find('span', class_='a-offscreen').text
        if(float(originalPrice[1:].strip()) > float(price[1:].strip())):
            print('Price dropped')
        time.sleep(delay*60*60) #hours * minutes * seconds

if __name__ == '__main__':
    #Change inputs here
    link = 'https://www.amazon.com/A315-24P-R7VH-Display-Quad-Core-Processor-Graphics/dp/B0BS4BP8FB/ref=sr_1_3?crid=366I9FOHLRTUY&keywords=laptop&qid=1704067439&sprefix=laptop%2Caps%2C150&sr=8-3&th=1'
    delay = 24 #in hours

    price_check(link, delay)
