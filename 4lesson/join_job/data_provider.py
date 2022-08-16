# Модуль который будет поставлять нам данные

import imp
from random import randint

# Получение температуры
def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)

# Получение давления
def get_preassure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)

# Измерние по скорости ветра
def get_wind_speed(sensor):
    if sensor == 1:
        return randint(0, 30)
    else:
        return randint(30, 50)

def data_collection(sensor = 1):
    return (get_temperature(sensor), get_preassure(sensor), get_wind_speed(sensor))