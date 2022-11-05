from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup


app = Flask(__name__, template_folder='template')


@app.route("/")
def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url='https://www.gismeteo.kz/weather-shymkent-5324', headers=headers)

    soup = BeautifulSoup(response.text)
    temp_data = soup.find_all('span', class_='unit unit_temperature_c')[0]

    operator_now = str(temp_data).split('"sign"')[1].split('>')[1].split('<')[0]
    int_tempr_now = str(temp_data).split('"sign"')[1].split('>')[2].split('<')[0]
    float_tempr_now = str(temp_data).split('"sign"')[1].split('>')[3].split('<')[0]

    temp_data = soup.find_all('span', class_='unit unit_temperature_c')[2]
    average_today_night = str(temp_data).split('unit_temperature_c">')[1].split('<')[0]

    average_today = soup.find_all('span', class_='unit unit_temperature_c')[3]
    average_today = str(average_today).split('temperature_c">')[1].split('<')[0]

    temperature_now = f'Прямо сейчас: {operator_now}{int_tempr_now}{float_tempr_now} С'
    print(temperature_now)

    temperature_today_tonight = f'Сегодня ночью: {average_today_night} С'
    print(temperature_today_tonight)

    temperature_today = f'Сегодня днем: {average_today} С'
    print(temperature_today)

    return render_template(
        'parser_data.html', temperature_now=temperature_now, temperature_today_tonight=temperature_today_tonight,
        temperature_today=temperature_today
    )
