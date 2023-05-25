# Подключение библиотеки для работы с датчиками и светодиодами
import RPi.GPIO as GPIO


# Конфигурация пинов
sensor_pin = 17  # Пин, к которому подключен датчик
led_pin = 18  # Пин, к которому подключен светодиод

# Константы для определения нормы корма и уровня батареи
feed_threshold = 500  # Пороговое значение корма
battery_threshold = 3.3  # Пороговое напряжение батареи

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)


# Функция для проверки уровня корма
def check_food_level():
    food_level = GPIO.input(sensor_pin)  # Считываем значение с датчика
    if food_level < feed_threshold:
        print("Низкий уровень корма! Желтый свет.")
        GPIO.output(led_pin, GPIO.HIGH)  # Включаем желтый светодиод
    else:
        print("Достаточный уровень корма.")
        GPIO.output(led_pin, GPIO.LOW)  # Выключаем светодиод


# Функция для проверки уровня батареи
def check_battery_level():
    battery_voltage = 3.5  # Пример значения напряжения батареи (замените на реальные показания)
    if battery_voltage < battery_threshold:
        print("Низкий уровень заряда батареи! Красный свет.")
        GPIO.output(led_pin, GPIO.LOW)  # Включаем красный светодиод
    else:
        print("Нормальный уровень заряда батареи.")
        GPIO.output(led_pin, GPIO.HIGH)  # Выключаем светодиод


print('Программа запущена.')
try:
    while True:
        check_food_level()    # Проверяем уровень корма
        check_battery_level()  # Проверяем уровень батареи

except KeyboardInterrupt:
    print('Программа завершена.')
    GPIO.cleanup()
