from datetime import datetime as dt
from time import time

# Метод отвечающий за логирование температуры
def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                    .format(time, data))

# Метод отвечающий за логирование давления
def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};pressure;{}\n'
                    .format(time, data))

# Метод отвечающий за логирование скорости ветра
def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, data))
