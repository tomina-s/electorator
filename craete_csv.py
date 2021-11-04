# -*- coding: utf-8 -*-
import pandas as pd
import random
import string
from sqlalchemy import create_engine

'''
Скрипт заполнения таблиц БД рандомными данными, походящими по типу.

Заоплняются таблицы:
    accounts_account
    accounts_role
    mainapp_candidate   
    mainapp_uik.
    
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


# path_to_DB = '***postgresql://username:password@localhost:5432/dbname'
path_to_DB = 'postgresql://huvalk:1234@localhost:8000/database'
ACCOUNTS_NUM = 10
table_name_accounts = 'accounts_account'

# генерация рандомных данных
password_series = pd.Series([gen_password(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])
# last_login - TODO: доделать генерацию полей - типа данных timestamp
last_login = pd.Series([gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])
name_series = pd.Series([gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])
username_series = pd.Series([gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])

df_accounts = pd.DataFrame({'password': password_series,
                            'last_login': name_series,
                            'name': name_series,
                            'username': username_series,
})


ACCOUNTS_ROLE_NUM = 10
table_name_accounts_role = 'accounts_role'

user_series = pd.Series([random.randint(1, 10) for _ in range(ACCOUNTS_ROLE_NUM)])
role_user_series = pd.Series([gen_string(random.randint(5, 10)) for _ in range(ACCOUNTS_ROLE_NUM)])
df_account_role = pd.DataFrame({'user': user_series,
                               'role_user': role_user_series
                                })

engine = create_engine(path_to_DB)
df_accounts.to_sql(table_name_accounts, engine)

engine = create_engine(path_to_DB)
df_account_role.to_sql(table_name_accounts_role, engine)


# print(df_accounts)
# df_accounts.to_csv('accounts.csv', index=False)
# csv_data = df_accounts.to_csv(index=False)
# print('\nCSV String:\n', csv_data)

