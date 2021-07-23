import requests
from bs4 import BeautifulSoup
products_to_track = [
    {
        "product_url": "https://www.amazon.in/gp/product/B08444WMFG/ref=ox_sc_act_title_1?smid=A14CZOWI0VEHLG&psc=1",
        "name": "Vivo V20",
        "target_price": 19500
    },
    {
        "product_url": "https://www.amazon.in/gp/product/B08LRDP2Q6/ref=ox_sc_act_title_2?smid=A14CZOWI0VEHLG&psc=1",
        "name": "Vivo Y51A",
        "target_price": 18000
    },
    {
        "product_url": "https://www.amazon.in/gp/product/B08VB2CMR3/ref=ox_sc_act_title_3?smid=A14CZOWI0VEHLG&psc=1",
        "name": "Oppo A74",
        "target_price": 18000
    },
    {
        "product_url": "https://www.amazon.in/gp/product/B085J1868F/ref=ox_sc_act_title_4?smid=A1EWEIV3F4B24B&psc=1",
        "name": "Samsung M51",
        "target_price": 21000
    },
    {
        "product_url": "https://www.amazon.in/gp/product/B07WJTMPPP/ref=ox_sc_act_title_5?smid=AQUYM0O99MFUT&psc=1",
        "name": "iQOO Z3",
        "target_price": 20000
    }
]
def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()
result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' -  \t' + ' Available at Target Price ' + ' Current Price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")

finally :
    result_file.close()