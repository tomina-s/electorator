# -*- coding: utf-8 -*-
import pandas as pd
import random
import string
from sqlalchemy import create_engine

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


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


# генерация рандомных данных
ACCOUNTS_NUM = 2
table_name_accounts = 'accounts_account'
accounts_data = {'password': [gen_password(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)],
                 'last_login': ['2020-05-16 08:36:38' for _ in range(ACCOUNTS_NUM)],
                 'name': [gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)],
                 'username': [gen_string(random.randint(5, 15)) for _ in range(ACCOUNTS_NUM)],
                 }

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


CANDIDATE_NUM = 8
table_name_candidate = 'mainapp_candidate'
candidate_name_series = pd.Series(['Васильев Олег Степанович', 'Лужков', 'Иванов', 'Собянин Сергей Семенович',
                                   'Собянин Иван', 'Антонова', 'Срегеев', 'Романов',
])
party_series = pd.Series('Партия' for _ in range(CANDIDATE_NUM))
info_series = pd.Series('Глава муниципального округа Таганский города Москвы' for _ in range(CANDIDATE_NUM))
sim_votes_series = pd.Series(random.randint(500, 650) for _ in range(CANDIDATE_NUM))
df_candidats = pd.DataFrame({'name': candidate_name_series,
                              'party': party_series,
                              'info': info_series,
                              'sum_votes': sim_votes_series,
                              'photo': pd.Series('file_name.jpg' for _ in range(CANDIDATE_NUM)),  # название файла .jpg
                              })
# print('df_candidats', df_candidats)
candidats = df_candidats.to_dict('dict')
# print('df_candidats', candidats)


table_name_uik = 'mainapp_uik'

# UIK_NUM = 3628
UIK_NUM = 2

id_uik = 6
uik_values = {'num_uik': [i for i in range(id_uik, UIK_NUM+id_uik)],
              'population': [random.randint(100, 300) for _ in range(UIK_NUM)],
              'status': [False for _ in range(UIK_NUM)],
              'sum_votes': [0 for _ in range(UIK_NUM)],
              'sum_numb_votes_fin': [0 for _ in range(UIK_NUM)],

              'presence': [0 for _ in range(UIK_NUM)],
              'perc_final_bul': [0 for _ in range(UIK_NUM)],
              'bad_form': [random.randint(0, 5) for _ in range(UIK_NUM)],
              'update_time': ['2020-05-16 08:36:38' for _ in range(UIK_NUM)],
              'num_tik': [1 for _ in range(UIK_NUM)],
              }


def insert_account(account_name):
    # print('account_name', account_name)
    sql = """INSERT INTO accounts_account(name)
             VALUES(%s) RETURNING id;"""
    # print('sql', sql)
    conn = None
    account_id = None
    try:
        # Подключение к существующей базе данных
        conn = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="***",
                                  host="huvalk.ru",
                                  port="8001",
                                  database="electorator")
        # Курсор для выполнения операций с базой данных
        cursor = conn.cursor()

        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(conn.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

        cursor.execute(sql, (account_name,))


        # get the generated id back
        account_id = cursor.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            conn.close()
    return account_id


def insert_candidate(name, party, info, sum_votes, photo):
    # print('candidate_name', candidate_name)
    sql = """INSERT INTO mainapp_candidate(name, party, info, sum_votes, photo)
             VALUES(%s,%s,%s,%s,%s) RETURNING id;"""
    # print('sql', sql)
    conn = None
    candidate_id = None
    try:
        # Подключение к существующей базе данных
        conn = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="***",
                                  host="huvalk.ru",
                                  port="8001",
                                  database="electorator")
        # Курсор для выполнения операций с базой данных
        cursor = conn.cursor()

        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(conn.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

        cursor.execute(sql, (name, party, info, sum_votes, photo,))

        # get the generated id back
        candidate_id = cursor.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            conn.close()
    return candidate_id


def insert_candidats(cand_info):
    sql = """INSERT INTO mainapp_candidate(name, party, info, sum_votes, photo)
             VALUES(%s,%s,%s,%s,%s) RETURNING id;"""
    conn = None
    PK_candadats = []

    try:
        conn = psycopg2.connect(user="postgres",
                                  password="***",
                                  host="huvalk.ru",
                                  port="8001",
                                  database="electorator")
        # Курсор для выполнения операций с базой данных
        cursor = conn.cursor()

        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(conn.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

        for idx in range(CANDIDATE_NUM):
            row = (cand_info['name'][idx], cand_info['party'][idx], cand_info['info'][idx], cand_info['sum_votes'][idx], cand_info['photo'][idx])
            cursor.execute(sql, row)

            # get the generated id back
            candidate_id = cursor.fetchone()[0]
            PK_candadats.append(candidate_id)

        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            conn.close()
    return PK_candadats


def insert_uik(uik_info, uik_num_value):
    sql = """INSERT INTO mainapp_uik(num_uik, population, status, sum_votes, sum_numb_votes_fin,
            presence, perc_final_bul, bad_form, update_time, num_tik)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    conn = None
    PK_uik = []
    try:
        conn = psycopg2.connect(user="postgres",
                                password="***",
                                host="huvalk.ru",
                                port="8001",
                                database="electorator")
        cursor = conn.cursor()
        print("Информация о сервере PostgreSQL")
        print(conn.get_dsn_parameters(), "\n")

        for idx in range(uik_num_value):
            row = []
            for key_field in uik_info.keys():
                row.append(uik_info[key_field][idx])
            row = tuple(row)
            print('row', row)
            cursor.execute(sql, row)

            candidate_id = cursor.fetchone()[0]
            PK_uik.append(candidate_id)

        conn.commit()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            conn.close()
    return PK_uik


def insert_account(accounts_info, accounts_num_value):
    sql = """INSERT INTO accounts_account(password, last_login, name, username)
            VALUES(%s,%s,%s,%s) RETURNING id;"""
    conn = None
    PK_values = []
    try:
        conn = psycopg2.connect(user="postgres",
                                password="***",
                                host="huvalk.ru",
                                port="8001",
                                database="electorator")
        cursor = conn.cursor()
        print("Информация о сервере PostgreSQL")
        print(conn.get_dsn_parameters(), "\n")

        for idx in range(accounts_num_value):
            row = []
            for key_field in accounts_info.keys():
                row.append(accounts_info[key_field][idx])
            row = tuple(row)
            print('row', row)
            cursor.execute(sql, row)

            new_id_as_PK = cursor.fetchone()[0]
            PK_values.append(new_id_as_PK)

        conn.commit()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            conn.close()
    return PK_values


def show_table_by_name(table_name):
    try:
        connection = psycopg2.connect(user="postgres",
                                password="***",
                                host="huvalk.ru",
                                port="8001",
                                database="electorator")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from " + table_name

        cursor.execute(postgreSQL_select_Query)
        # print("Selecting rows from mobile table using cursor.fetchall")
        table_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in table_records:
            print('row', row)
            # print("Id = ", row[0], )
            # print("Model = ", row[1])
            # print("Price  = ", row[2], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# print(insert_account('ac_name'))
# print(insert_candidate(candidats['name'][0], candidats['party'][0], candidats['info'][0], candidats['sum_votes'][0], candidats['photo'][0]))

# Вставка строк в таблицу Кандидаты
# PK_candadats = insert_candidats(candidats)
# print('PK_candadats', PK_candadats)

# PK_uik = insert_uik(uik_values, uik_num_value=UIK_NUM)
# print('PK_uik', PK_uik)

# Вставка ACCOUNTS_NUM числа строк в таблицу Аккаунты
# PK_account = insert_account(accounts_data, accounts_num_value=ACCOUNTS_NUM)
# print('PK_account', PK_account)

# show_table_by_name(table_name='mainapp_uik')
show_table_by_name(table_name='accounts_account')