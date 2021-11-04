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


path_to_DB = 'postgresql://postgres:***@***.ru:8001/electorator'
ACCOUNTS_NUM = 10
table_name_accounts = 'accounts_account'

# генерация рандомных данных
password_series = pd.Series([gen_password(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])
# last_login - типа данных timestamp
last_login_series = pd.Series(['2020-05-16 08:36:38' for _ in range(ACCOUNTS_NUM)])
name_series = pd.Series([gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])
username_series = pd.Series([gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)])

df_accounts = pd.DataFrame({'password': password_series,
                            'last_login': last_login_series,
                            'name': name_series,
                            'username': username_series,
})

ACCOUNTS_ROLE_NUM = 10
table_name_accounts_role = 'accounts_role'
USER_ROLE_MGIK = 'МГИК'
USER_ROLE = ['ТИК', 'УИК']
user_series = pd.Series([idx for idx in range(5, 5+ACCOUNTS_ROLE_NUM)])
role_user_series = pd.Series(USER_ROLE[random.randint(0, 1)] for _ in range(ACCOUNTS_ROLE_NUM))
df_account_role = pd.DataFrame({'user_id': user_series,
                               'role_user': role_user_series
                                })
# print('role_user_series\n', type(role_user_series))
# print('df_account_role', df_account_role)
engine = create_engine(path_to_DB)

df_accounts.to_sql(table_name_accounts, engine, if_exists='append', index=False)  # if_exists='append' / replace

engine = create_engine(path_to_DB)
# print(engine)
df_account_role.to_sql(table_name_accounts_role, engine, if_exists='replace', index=False)

CANDIDATE_NUM = 8
table_name_candidate = 'mainapp_candidate'
candidate_name_series = pd.Series(['Петров Иван Степанович', 'Лужков', 'Иванов', 'Собянин Сергей Семенович',
                                   'Собянин Иван', 'Антонова', 'Срегеев', 'Романов',
])
party_series = pd.Series('Партия' for _ in range(CANDIDATE_NUM))
info_series = pd.Series('Глава муниципального округа Таганский города Москвы' for _ in range(CANDIDATE_NUM))
sim_votes_series = pd.Series(random.randint(500, 650) for _ in range(CANDIDATE_NUM))
df_candidates = pd.DataFrame({'name': candidate_name_series,
                              'party': party_series,
                              'info': info_series,
                              'sum_votes': sim_votes_series,
                              'photo': pd.Series('file_name.jpg' for _ in range(CANDIDATE_NUM)),  # название файла .jpg
                              })
# print('df_candidates', df_candidates)
df_candidates.to_sql(table_name_candidate, engine, if_exists='replace', index=False)

table_name_uik = 'mainapp_uik'

UIK_NUM = 3628
df_uik = pd.DataFrame({'num_uik': pd.Series(i for i in range(1, UIK_NUM+1)),
                       'num_tik': pd.Series(1 for _ in range(1, UIK_NUM+1)),
                       'population': pd.Series(random.randint(100, 300) for _ in range(UIK_NUM)),
                       'sum_numb_votes_fin': pd.Series(0 for _ in range(UIK_NUM)),
                       'presence': pd.Series(0 for _ in range(UIK_NUM)),
                       'perc_final_bul': pd.Series(0 for _ in range(UIK_NUM)),
                       'bad_form': pd.Series(random.randint(0, 5) for _ in range(UIK_NUM)),
                       'update_time': pd.Series('2020-05-16 08:36:38' for _ in range(UIK_NUM)),
                       })
# print('df_uik\n',df_uik)
df_candidates.to_sql(table_name_candidate, engine, if_exists='append', index=False)
