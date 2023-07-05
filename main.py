import pytesttest_data = [("10FA0E00", {'field1': 'Low',                           'field2': '00',                           'field3': '01',                           'field4': '00',                           'field5': '00',                           'field6': '01',                           'field7': '00',                           'field8': 'Very High',                           'field9': '00',                           'field10': '00'}),             ]# Format settings - array [sett_byte1 as dict {bit: [size, 'field_name']}, sett_byte2,# sett_byte3, sett_byte4]device_settings = [{0: [3, 'field1'],                    3: [1, 'field2'],                    4: [1, 'field3'],                    5: [3, 'field4']},                   {0: [1, 'field5'],                    1: [1, 'field6'],                    2: [1, 'field7'],                    3: [3, 'field8'],                    },                   {0: [1, 'field9'],                    5: [1, 'field10']                    },                   {}                   ]field1 = {'0': 'Low',          '1': 'reserved',          '2': 'reserved',          '3': 'reserved',          '4': 'Medium',          '5': 'reserved',          '6': 'reserved',          '7': 'High',          }field4 = {'0': '00',          '1': '10',          '2': '20',          '3': '30',          '4': '40',          '5': '50',          '6': '60',          '7': '70',          }field8 = {'0': 'Very Low',          '1': 'reserved',          '2': 'Low',          '3': 'reserved',          '4': 'Medium',          '5': 'High',          '6': 'reserved',          '7': 'Very High',          }# 1. Написать функцию которая будет парсить пейлоад команды от датчика и возвращать# значения всех параметров. Проверочные данные: пейлоад = "10FA0E00"def get_data_from_payload(payload):    # конвертируем в тип данных байт эррей и убираем не нужные значения    byte_array = bytearray.fromhex(payload[:-2])    array_settings_byte = []    for byte in byte_array:        # разделение в список по байтно        array_settings_byte.append(byte)    parsed_data = {}    for index, byte in enumerate(array_settings_byte):        # получаем байт в двоичной системе в виде 8 бит и сразу же инвертируем        string_byte_revers = bin(byte)[2:].zfill(8)[::-1]        # распаковка сразу нескольких значений из поля        for start_bit, (shift, name_field) in device_settings[index].items():            res = string_byte_revers[start_bit: start_bit + shift]            if len(res) == 3:                parsed_data[name_field] = globals()[name_field][str(int(res, 2))]            else:                parsed_data[name_field] = '0' + str(res)    return parsed_datatest_data_1 = [("AAF10F00", {'field1': 'reserved',                             'field2': '01',                             'field3': '00',                             'field4': '50',                             'field5': '01',                             'field6': '00',                             'field7': '00',                             'field8': 'reserved',                             'field9': '01',                             'field10': '00'}),             ]@pytest.mark.parametrize("payload, result", [(test_data[0][0], test_data[0][1]),                                             (test_data_1[0][0], test_data_1[0][1])                                             ])def test_parser(payload, result):    assert get_data_from_payload(payload) == resultif __name__ == '__main__':    print(get_data_from_payload('10FA0E00'))