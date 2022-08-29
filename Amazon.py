import bs4
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/s?k=laptop&sprefix=lap%2Caps%2C361&ref=nb_sb_ss_ts-doa-p_1_3"
header={'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'session-id=143-1771339-3409448; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:PK"; ubid-main=134-0245857-5945768; session-token=klbXv3Hlr1jVB7tWSGISLqZvS6NlwFJjR9yljFK3Q/FSkSCUDvhEfentyPsIt4A3DbS0Xk+H0Bp8GvE+EaChIHhJaShw94yqzV2tkG2sTZoebN45DfoPMN7d3KKZqAsOLtkPE4xfChnk8xVP8MjKerg164gj3trANeTun0xX1bTuooa8YNnXntT4lhVxPjp978amfRLDE7UthEfTroN1ew6EAL73zOU+; skin=noskin; csm-hit=tb:s-X26JCXAPS486YTN3FW4A|1661627638191&t:1661627639202&adb:adblk_no',
'device-memory' : '8',
'downlink': '0.4',
'dpr': '1',
'ect': '4g',
'referer': 'https://www.amazon.com/',
'rtt': '150',
'sec-ch-device-memory': '8',
'sec-ch-dpr': '1',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-ch-viewport-width': '1366',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' }


html_text = requests.get(url, headers=header).text
soup = BeautifulSoup(html_text, 'html.parser')
product = soup.findAll('div', {'class': "s-result-item"})
# print(len(main_data))
for data in product:
     item = data.findAll('h2', {'class': "a-size-mini a-spacing-none a-color-base s-line-clamp-2"})

     for datas in item:
        name = datas.find('span', {'class' : 'a-size-medium a-color-base a-text-normal'})
        print(name.text)


import bs4
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/s?k=hp+laptops&crid=1SMIQQUBGNHLV&sprefix=hp+la%2Caps%2C325&ref=nb_sb_ss_ts-doa-p_2_5"
header={'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'session-id=143-1771339-3409448; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:PK"; ubid-main=134-0245857-5945768; skin=noskin; session-token=m594zwqnNQe8lpRdZ2HxRr/PxZNfA0Fl2lvEILb1G8AmNccFBzVipsMO3MRAkndzCBEJvKINtrBXYqvDPFRtin8T3x12RuymZm/acdvD4SR0qn/WEVFDYkLGK+sGBildj+N+xw+6uaBlvndVIZtMB6Ti+18ug5LbbaUFwoNqko3tGH3LGIxtBb8r0aA9OIz8HML4HKxlzWZGorbdDMD6KAmw+0zFrSq2; csm-hit=tb:s-BN52B2V0N7MEAJHRQ3J3|1661684565258&t:1661684566287&adb:adblk_no',
'device-memory': '8',
'downlink': '1.5',
'dpr': '1',
'ect': '3g',
'rtt': '300',
'sec-ch-device-memory': '8',
'sec-ch-dpr': '1',
'sec-ch-ua': 'Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104" ',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-ch-viewport-width': '1366',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

html_text = requests.get(url, headers=header).text
soup = BeautifulSoup(html_text,'html.parser')
product=soup.findAll('div', {'class':"s-result-item"})
for data in product:
    item = data.findAll('div', {'class' : "a-section a-spacing-small a-spacing-top-small"})
    for datas in item:
         name_specifications=datas.find('span' ,{'class' : "a-size-medium a-color-base a-text-normal"})
         print(name_specifications.text)
         price =datas.find('span' , { 'class' : 'a-offscreen'})
         print(price)
         rating = datas.find('span', {'class': 'a-icon-alt'})
         print(rating.text)
         print(" ")

                                                            🙌🙌