import requests
import json


stocks = 'https://api-seller.ozon.ru/v1/report/stock/create'
report = 'https://api-seller.ozon.ru/v1/report/info'
key = ''

headers = {
            'Host':'api-seller.ozon.ru',
            'Client-Id':'',
            'Api-Key':'',
            'Content-Type':'application/json'
        }

data = {
        'language':'DEFAULT'
    }

while True:
    post_stocks = requests.post(stocks, json=data, headers=headers)
    code = post_stocks.json()['result']['code']
    # print(type(code))
    post_report = requests.post(report, json = {'code':code}, headers=headers)
    print(post_report.content)
    if post_report.json()['result']['status'] == 'success':
        break
with open('report.csv', 'wb') as f:
    f.write(requests.get(post_report.json()['result']['file'], headers=headers).content)

