# -*- coding: utf-8 -*-
import pandas as pd
# import csv
import random
import string

'''
1 прописать формат данных таблицы 
 - создать дата фрейм

- создать csv файл
- загрузить в БД

'''


def gen_password(length):
    """Создать случайную буквенно-цифровую строку длиной length."""
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def gen_string(length):
    """Создать случайную буквеенную строку длиной length."""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


ACCOUNTS_NUM = 10
table_name_accounts = 'accounts_account'

# генерация рандомных данных
password_series = pd.Series([gen_password(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])
# print("OUTPUT",  password_series)
# last_login - TODO: доделать генерацию полей - типа данных timestamp
last_login = pd.Series([gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])
name_series = pd.Series([gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])
username_series = pd.Series([gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])

# создание DataFrame
# colums_account = ['password', 'last_login', 'name', 'username']
df = pd.DataFrame({'password': password_series,
                   'last_login': name_series,
                   'name': name_series,
                   'username': username_series,
})
# print(df)

# df.to_csv('accounts.csv', index=False)
csv_data = df.to_csv(index=False)
print('\nCSV String:\n', csv_data)

# file_writer = csv.writer(w_file, delimiter = "\t")
