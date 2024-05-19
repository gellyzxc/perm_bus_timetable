import requests
import html
from bs4 import BeautifulSoup
import html_to_json
from datetime import datetime

def getInfo(stop_id, bus_name):
    page = requests.get(f'https://m.gortransperm.ru/stoppoint-arrival-times/{stop_id}/')

    data = html.unescape(page.text)

    soup = BeautifulSoup(data, "html.parser")

    data = soup.find_all('li')
    if (data == []):
        return []
    del data[0]

    data = html_to_json.convert(str(data))
    if (bus_name == 'null'):
        pass
    else:
        keys = [x for x in data.keys()]
        for key in keys:
            if (key != bus_name):
                del data[key]

    result = {}
    now = datetime.now()
    now_splitted = str(now).split(' ')
    for item in data['li']:
        temp = []
        for arrival in item['span']:
            value = now_splitted[0] + ' ' + arrival['_value']
            start = datetime.strptime(value,  '%Y-%m-%d %H:%M') 
            temp.append({"time": arrival['_value'], "difference": round((start - now).total_seconds() / 60) - 300})
        result[item['_value'][:-2]] = temp

    return result

def getBuses():
    page = requests.get(f'https://m.gortransperm.ru/routes-list/0/')
    
    data = html.unescape(page.text)

    soup = BeautifulSoup(data, "html.parser")

    data = soup.find_all('li')
    if (data == []):
        return []
    
    data = html_to_json.convert(str(data))

    result = []
    for item in data['li']:
        result.append({
            "name": item['a'][0]['_value'],
            "link": item['a'][0]['_attributes']['href'].split('/')[2]
        })
    return result

def getBusStops(bus_id):
    page = requests.get(f'https://m.gortransperm.ru/route/{bus_id}/')
    
    data = html.unescape(page.text)

    soup = BeautifulSoup(data, "html.parser")

    data = soup.find_all('li')
    if (data == []):
        return []
    
    data = html_to_json.convert(str(data))

    result = []
    for item in data['li']:
        result.append({
            "name": item['a'][0]['_value'],
            "link": item['a'][0]['_attributes']['href'].split('/')[3]
        })
    return result

if __name__ == "__main__":
    stop_id = input('stop id: ')

    # res = getInfo(stop_id=stop_id)
    # print(res)