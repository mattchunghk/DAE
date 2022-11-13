import json
from pymongo import MongoClient
import pandas as pd
import http.client

client = MongoClient('localhost', 27017)
db = client.estate


# f = open('midland-1667461371794.json')
# data = json.load(f)

conn = http.client.HTTPSConnection("www.midlandici.com.hk")

payload = ""

headers = {
    'Accept': "application/json, text/plain, */*",
    'Accept-Language': "en-US,en;q=0.9,it;q=0.8",
    'Connection': "keep-alive",
    'Cookie': "PHPSESSID=s47kj15liaarhcuj5fos2jbdt2; id=arLodm3TG66ZG8LmLp6avIsuUR4lcLZn; TSCvalue=big5; filters={%22tx_type%22:[]%2C%22keywords%22:%22{%5C%22suggestionWord%5C%22:%5C%22%E5%AD%96%E6%B2%99%E8%A1%97%5C%22%2C%5C%22type%5C%22:%5C%22free_text%5C%22%2C%5C%22value%5C%22:%5C%22%E5%AD%96%E6%B2%99%E8%A1%97%5C%22%2C%5C%22ics%5C%22:%5C%22%5C%22}%22%2C%22last_clicked%22:%22S095278%22%2C%22marked_cursor%22:2}; sorting=null; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%220777af554f9cb0dfbf388983f6ed86b3%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22118.140.121.58%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A117%3A%22Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_15_7%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F107.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1667461101%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22lang%22%3Bs%3A5%3A%22zh-HK%22%3B%7Da90c33219e65e9ed3532f30c4fe8388623b3f971; _gid=GA1.3.1446225028.1667461102; _ga=GA1.1.770975343.1667296978; _ga_PET8PT45VP=GS1.1.1667461102.3.1.1667461278.0.0.0",
    'Referer': "https://www.midlandici.com.hk/ics/property/find/shops",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': '"macOS"'
}

conn.request(
    "GET", "/ics/property/stock/stockFilterJson?ics_type=s&page_size=8728&=", payload, headers)

res = conn.getresponse()
data = res.read()

data = json.loads(data.decode("utf-8"))


def main():
    info_arr = []
    for info in data['stocks']:
        if int(info['rent']) > 0:
            info_dict = {
                '_id': info['gstock_id'],
                'region': info['region'],
                'rent': info['rent'],
                'area': info['area'],
                'lat': info['lat'],
                'lng': info['lng'],
                'address': info['eng_addr_name'],
                'dist': info['dist_eng_name'],
            }
            # info_arr.append(info_dict)

            db.midland.insert_one(info_dict)
    # print(pd.DataFrame(info_arr))


# f.close()


if __name__ == "__main__":
    main()
    pass
