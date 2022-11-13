from google.cloud import bigquery
from pymongo import MongoClient
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
load_dotenv()


client = bigquery.Client()

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page(
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36")
    for page_number in range(1, 20):
        page.goto(
            "https://www.openrice.com/zh/hongkong/restaurants?where=%E4%B8%8A%E7%92%B0&page={}".format(page_number))

        # Use document query selector to get the data
        restaurant_texts = page.locator('.title-name>a').all_text_contents()
        restaurant_price = page.locator(
            '.icon-info-food-price>span').all_text_contents()
        restaurant_address = page.locator(
            ".address>span").all_text_contents()
        openrice_data = client.get_table(
            'dea-proj.dea_proj_data.openrice')
        for i in range(len(restaurant_texts)):

            result = client.insert_rows_json(openrice_data, [{'name': restaurant_texts[i],
                                                             'price': restaurant_price[i], 'address': restaurant_address[i].strip()}])
            # db.openrice.insert_one({'name': restaurant_texts[i],
            #                         'price': restaurant_price[i], 'address': restaurant_address[i].strip()})
            # print({'name': restaurant_texts[i],
            #       'price': restaurant_price[i], 'address': restaurant_address[i].strip()})

        # restaurant_texts = page.query_selector(".title-name>a")
        # restaurant_price = page.query_selector(".icon-info-food-price>span")
        # restaurant_address = page.query_selector(".address>span")
        # name = restaurant_texts.inner_text()
        # price = restaurant_price.inner_text()
        # address = restaurant_address.inner_text()
        # print({'name': name, 'price': price, 'address': address})

        # db.openrice.insert_one(
# browser.close()  # {'name': name, 'price': price, 'address': address})
