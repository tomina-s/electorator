# -*- coding: utf-8 -*-
import pandas as pd
import psycopg2

# import random
# import string
# from sqlalchemy import create_engine


'''
Скрипт заполнения таблиц БД данными из эсель файла.

Заоплняются таблицы:
    протокол 1

'''


file_name = 'electorator_data.xlsx'


def insert_protocol_1_fk_in(protocol_1_info, num_value, FK_num_uik):
    sql = """INSERT INTO mainapp_protocol1(num_protocol_1, status, sum_bul, sum_final_bul, bad_form, transfer_time,
     num_uik_id) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    conn = None
    PK_values = []
    try:
        conn = psycopg2.connect(user="postgres",
                                password="***",
                                host="huvalk.ru",
                                port="8001",
                                database="electorator")
        cursor = conn.cursor()

        for idx in range(num_value):
            row = []
            for key_field in protocol_1_info.keys():
                row.append(protocol_1_info[key_field][idx])
            row.append(FK_num_uik[idx])
            print('row', tuple(row))
            cursor.execute(sql, tuple(row))

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


def insert_protocol_1(protocol_1_info, num_value):
    sql = """INSERT INTO mainapp_protocol1(num_protocol_1, status, sum_bul, sum_final_bul, bad_form, transfer_time,
     num_uik_id) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    conn = None
    PK_values = []
    try:
        conn = psycopg2.connect(user="postgres",
                                password="***",
                                host="huvalk.ru",
                                port="8001",
                                database="electorator")
        cursor = conn.cursor()

        for idx in range(num_value):
            row = []
            for key_field in protocol_1_info.keys():
                row.append(protocol_1_info[key_field][idx])
            print('row', tuple(row))
            cursor.execute(sql, tuple(row))

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


df = pd.read_excel(file_name, sheet_name='protocol1')
# tik_names = df['tik_name'].tolist()

colums_names = list(df.columns.values)
# print(colums_names)
dict_protocol_1 = {name: df[name].tolist() for name in colums_names}


# Вставка в Протокол 1 из экселя и захардкоденные FK
# FK_num_uik = ['1', '2']
# PK_protocol_1 = insert_protocol_1_fk_in(dict_protocol_1, len(df), FK_num_uik)

# Вставка в Протокол 1 из экселя (FK заносится в эксле)
PK_protocol_1 = insert_protocol_1(dict_protocol_1, len(df))

