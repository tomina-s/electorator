import os
import pandas as pd
import psycopg2


'''
Скрипт заполнения таблиц БД данными из эсель файла.

Заоплняются таблицы:
    протокол 1
    протокол 2
    ТИК
    uikprotocol1
    Кандидат
    УИК.
Последовательность заполнения таблиц: кандидаты, тик, уик, протокол 1, уик_протокол 1.   

'''


file_name = 'electorator_data_many_2.xlsx'

def connect_to_db():
    conn = psycopg2.connect(user="postgres",
                            password=os.environ.get('POSTGRES_PASSWORD'),
                            host=os.environ.get('POSTGRES_HOST'),
                            port=os.environ.get('POSTGRES_PORT'),
                            database=os.environ.get('POSTGRES_DB'))
    cursor = conn.cursor()
    print("Информация о сервере PostgreSQL")
    print(conn.get_dsn_parameters(), "\n")
    return conn, cursor


def insert_protocol_1_fk_in(protocol_1_info, num_value, FK_num_uik):
    sql = """INSERT INTO mainapp_protocol1(num_protocol_1, status, sum_bul, sum_final_bul, bad_form, transfer_time,
     num_uik_id) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    conn = None
    PK_values = []
    try:
        conn, cursor = connect_to_db()

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
        conn, cursor = connect_to_db()

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


def insert_protocol_2(protocol_2_info, num_value):
    sql = """INSERT INTO mainapp_protocol2(num_protocol_2, candidate_votes,	transfer_time, name_id,	num_uik_id)
    VALUES(%s,%s,%s,%s,%s) RETURNING id;"""
    conn = None
    PK_values = []
    try:
        conn, cursor = connect_to_db()

        for idx in range(num_value):
            row = []
            for key_field in protocol_2_info.keys():
                row.append(protocol_2_info[key_field][idx])
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


def insert_tik(tik_info, num_value):
    sql = """INSERT INTO mainapp_tik(population, open_uik, sum_votes, sum_numb_votes_fin, presence,
    perc_final_bul, bad_form, update_time, num_tik) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    conn = None
    PK_values = []
    try:
        conn, cursor = connect_to_db()

        for idx in range(num_value):
            row = []
            for key_field in tik_info.keys():
                row.append(tik_info[key_field][idx])
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


def insert_uikpr_1(tik_info, num_value):
    sql = """INSERT INTO mainapp_uikprotocol1(id_protocol1_id, id_uik_id) VALUES(%s,%s) RETURNING id;"""
    conn = None
    PK_values = []
    try:
        conn, cursor = connect_to_db()

        for idx in range(num_value):
            row = []
            for key_field in tik_info.keys():
                row.append(tik_info[key_field][idx])
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


def insert_candidate(candidate_info, num_value):
    sql = """INSERT INTO mainapp_candidate(name, party, info, sum_votes, photo, birthday, birthday_place, education,
    polit_position, position, work)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    conn = None
    PK_values = []
    try:
        conn, cursor = connect_to_db()

        for idx in range(num_value):
            row = []
            for key_field in candidate_info.keys():
                row.append(candidate_info[key_field][idx])
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


def insert_uik(uik_info, num_value):
    sql = """INSERT INTO mainapp_uik(num_uik, population, status, sum_votes, sum_numb_votes_fin, presence,
    perc_final_bul, bad_form, update_time, num_tik)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    PK_values = []
    for idx in range(num_value):
        row = []
        for key_field in uik_info.keys():
            row.append(uik_info[key_field][idx])
        print('row', tuple(row))
        cursor.execute(sql, tuple(row))

        new_id_as_PK = cursor.fetchone()[0]
        PK_values.append(new_id_as_PK)
    return PK_values


df_candidate = pd.read_excel(file_name, sheet_name='candidate')
colums_names = list(df_candidate.columns.values)
dict_candidate = {name: df_candidate[name].tolist() for name in colums_names}

df_pr_1 = pd.read_excel(file_name, sheet_name='protocol1')
colums_names = list(df_pr_1.columns.values)
dict_protocol_1 = {name: df_pr_1[name].tolist() for name in colums_names}

df_pr_2 = pd.read_excel(file_name, sheet_name='protocol2')
colums_names = list(df_pr_2.columns.values)
dict_protocol_2 = {name: df_pr_2[name].tolist() for name in colums_names}

df_tik = pd.read_excel(file_name, sheet_name='tik')
colums_names = list(df_tik.columns.values)
dict_tik = {name: df_tik[name].tolist() for name in colums_names}

df_uikprotocol1 = pd.read_excel(file_name, sheet_name='uikprotocol1')
colums_names = list(df_uikprotocol1.columns.values)
dict_uikprotocol1 = {name: df_uikprotocol1[name].tolist() for name in colums_names}


df_uik = pd.read_excel(file_name, sheet_name='uik')
colums_names = list(df_uik.columns.values)
dict_uik = {name: df_uik[name].tolist() for name in colums_names}


# Вставка в candidate
# PK_tik = insert_candidate(dict_candidate, len(df_candidate))


# Вставка в Протокол 1 из экселя и захардкоденные FK
# FK_num_uik = ['1', '2']
# PK_protocol_1 = insert_protocol_1_fk_in(dict_protocol_1, len(df_pr_1), FK_num_uik)

# Вставка в Протокол 1 из экселя (FK заносится в эксле)
# PK_protocol_1 = insert_protocol_1(dict_protocol_1, len(df_pr_1))
# print(PK_protocol_1)

# Вставка в Протокол 2 из экселя (FK заносится в эксле)
# PK_protocol_2 = insert_protocol_2(dict_protocol_2, len(df_pr_2))

# Вставка в ТИК из экселя
# PK_tik = insert_tik(dict_tik, len(df_tik))
# print(PK_tik)

# Вставка в uikprotocol1 - таблица связей из экселя
# PK_uikpr_1 = insert_uikpr_1(dict_uikprotocol1, len(df_uikprotocol1))
# print(PK_uikpr_1)


try:
    conn = None
    conn, cursor = connect_to_db()

    # Вставка в УИК
    PK_uik = insert_uik(dict_uik, len(df_uik))
    print(PK_uik)


except (Exception, psycopg2.DatabaseError) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        conn.commit()

        conn.close()
