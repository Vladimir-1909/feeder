# Кормушка (Feeder) 

Кормушка для животных с датчиком уровня корма и индикатором светодиода

## Описание

Этот проект представляет собой простую кормушку, оснащенную датчиком уровня корма и индикатором светодиода. Когда уровень корма становится ниже определенной нормы, датчик активируется и индикатор светодиода меняет цвет на желтый, указывая на необходимость пополнить корм. Кроме того, если устройство, работающее на основе этого кода, обнаруживает низкий уровень заряда батареи, светодиод будет мигать красным цветом.

## Установка

1. Клонируйте репозиторий с помощью команды:
```
git clone https://github.com/Vladimir-1909/feeder.git
```

2. Перейдите в каталог проекта:
```
cd feeder
```

3. Установите необходимые зависимости с помощью команды:
```
pip install -r requirements.txt
```

## Использование

1. Подключите датчик уровня корма к соответствующему пину на Raspberry Pi (например, пин 17).
2. Подключите светодиод к соответствующему пину (например, пин 18).
3. Запустите код на Raspberry Pi с помощью команды:
```python
python main.py
```

## Параметры конфигурации

В файле `main.py` можно настроить следующие параметры:

- `sensor_pin`: Пин Raspberry Pi, к которому подключен датчик уровня корма.
- `led_pin`: Пин Raspberry Pi, к которому подключен светодиод.
- `feed_threshold`: Пороговое значение уровня корма, ниже которого считается, что корма мало.
- `battery_threshold`: Пороговое напряжение батареи, ниже которого считается, что заряд низкий.

##