import requests

response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

city_air = response_data.json()

rows = (city_air['RealtimeCityAir']['row'])

for row in rows:
    if row['PM10'] < 30:

        print(row['MSRSTE_NM'],row['PM10'])

