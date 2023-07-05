### Что сказал датчик?

Датчики Ajax беспроводные, работают на батарейках до 7ми лет, поэтому они вынуждены
передавать свои данные тщательно упакованными структурами.
Например четырьмя байтами информации датчик может передать информацию по 10 своим параметрам.
Датчик отправляет пакет на хаб с данными (далее "пейлоад") "10FA0E00", хаб должен расшифровать
этот набор байтов и выдать уже обработанные данные по всем 10 параметрам, в таком виде:
    {'field1': 'Low',
     'field2': '00',
     'field3': '01',
     'field4': '00',
     'field5': '00',
     'field6': '01',
     'field7': '00',
     'field8': 'Very High',
     'field9': '00',
     'field10': '00'}

Структуру параметров в датчике можно представить следующим образом:
#Format settings - array [sett_byte1 as dict {bit: [size, 'field_name']}, sett_byte2,
sett_byte3, sett_byte4]
device_settings = [{0: [3, 'field1'],
                    3: [1, 'field2'],
                    4: [1, 'field3'],
                    5: [3, 'field4']},
                   {0: [1, 'field5'],
                    1: [1, 'field6'],
                    2: [1, 'field7'],
                    3: [3, 'field8'],
                   },
                   {0: [1, 'field9'],
                    5: [1, 'field10']
                   },
                   {}
                  ]

Это список байтов (4), в которых каждому биту соответствует какой-то параметр (первый
элемент в списке соответствующего бита). Некоторые параметры могут занимать больше одного
бита, например field1, он занимает 3 бита, о чем говорит нулевой элемент списке
соответствующего бита. Для параметров, которые в пейлоаде занимают больше 1 бита даны
следующие переменные:
    field1 = {'0': 'Low',
              '1': 'reserved',
              '2': 'reserved',
              '3': 'reserved',
              '4': 'Medium',
              '5': 'reserved',
              '6': 'reserved',
              '7': 'High',
              }
    field4 = {'0': '00',
              '1': '10',
              '2': '20',
              '3': '30',
              '4': '40',
              '5': '50',
              '6': '60',
              '7': '70',
              }
    field8 = {'0': 'Very Low',
              '1': 'reserved',
              '2': 'Low',
              '3': 'reserved',
              '4': 'Medium',
              '5': 'High',
              '6': 'reserved',
              '7': 'Very High',
              }

Например, параметр field4, который занимает 3 бита, в битовой маске равен 011, что
в десятичной системе измерения равно 3, из этого следует, что параметр field4 равен 30.

### Задание:
1. Написать функцию которая будет парсить пейлоад команды от датчика и возвращать
значения всех параметров. Проверочные данные: пейлоад = "10FA0E00", функция должна вернуть структуру:
    {'field1': 'Low',
     'field2': '00',
     'field3': '01',
     'field4': '00',
     'field5': '00',
     'field6': '01',
     'field7': '00',
     'field8': 'Very High',
     'field9': '00',
     'field10': '00',
    }

2. Написать тест на эту функцию используя pytest. Тест получает на вход пейлоад и
ожидаемый результат. Тест должен быть параметризированым несколькими вариантами.


