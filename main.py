import json
import time
import re
from tqdm import tqdm

path = 'D:\\Projects\\lab2\\111.txt'
data = json.load(open(path, encoding='windows-1251'))


class Validator:

    def check_email(email : str) -> bool:
        if type(email) != str:
            return False
        pattern = '^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$'
        if re.match(pattern, email):
            return True
        return False

    def check_height(height : str) -> bool:
        pattern = '[1-2]\.\d{2}'
        if re.match(pattern, str(height)) is not None:
            return False

    def check_inn(inn : str) -> bool:
        if len(inn) == 12:
            return True
        return False

    def check_passport_num(passport : int) -> bool: ###########
        if len(passport(int)) == 6:
            return True
        return False

    def check_address(address : str) -> bool:
        pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
        if type(address) != str:
            return False
        if re.match(pattern, address):
            return True
        return False

    def check_type_int(num) -> bool:
        if type(num) != int:
            return False
        return True

    def check_type_string(string) -> bool:
        if type(string) != str:
            return False
        return True


right_data = list()
email = 0
height = 0
inn = 0
passport = 0
university = 0
work_experience = 0
political_view = 0
worldview = 0
address = 0


def check():  # демонстрация прогресса обработки при помощи tdqm
    time.sleep(1)


with tqdm(total=len(data)) as progressbar:
  for person in data:
    temp = True
    if not Validator.check_email(person['email']):
        email += 1
        temp = False
    if not Validator.check_height(person['height']):
        height += 1
        temp = False
    if not Validator.check_inn(person['inn']):
        inn += 1
        temp = False
    if not Validator.check_passport_num(person['passport_number']):
        passport += 1
        temp = False
    if not Validator.check_type_string(person['university']):
        university += 1
        temp = False
    if not Validator.check_type_int(person['work_experience']):
        work_experience += 1
        temp = False
    if not Validator.check_type_string(person['political_views']):
        political_view += 1
        temp = False
    if not Validator.check_type_string(person['worldview']):
        worldview += 1
        temp = False
    if not Validator.check_address(person['address']):
        address += 1
        temp = False
    if temp:
        right_data.append(person)
    progressbar.update(5)

