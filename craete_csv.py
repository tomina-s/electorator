# -*- coding: utf-8 -*-
import pandas as pd
# import csv
import random
import string

'''
1 прописать формат данных таблицы 

- создать csv файл

'''


table_name_accounts = 'accounts_account'
# прописать название колонок
colums_accounts = ['password', 'last_login', 'name', 'username']

# создать оъект pandas

# для пароля
def gen_password(length):
    '''Создать случайную буквенно-цифровую строку длиной length.'''
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    # print(rand_string)
    return rand_string
    # rand_string = ''.join(random.sample(letters_and_digits, length))
    # print("Alphanum Random string of length", length, "is:", rand_string)


gen_password(6)

accounts_num = 10
# нагенерировать рандомные (списки мб) данных
password_list = []
for _ in range(accounts_num):
    password_list.append(gen_password(random.randint(5, 15)))
# print('password_list', password_list)

password_series = pd.Series([gen_password(random.randint(5, 15)) for _ in range(accounts_num)])
print(password_series)
# last_login
name_series = pd.Series(['Alice' for _ in range(accounts_num)])
username_series = pd.Series(['' for _ in range(accounts_num)])
# print("OUTPUT",  password_series)
df = pd.DataFrame(password_series)
# print(df)


# df = pd.DataFrame([[1,'Bob', 'Builder'],
#                   [2,'Sally', 'Baker'],
#                   [3,'Scott', 'Candle Stick Maker']],
# columns=['id','name', 'occupation'])
#
# print(df)
# #
#
# changes = pd.read_excel('Changes.xlsx', encoding='utf-8')
# initial_list = []
# final_list = []
# initial_list_start = changes['initial'].tolist()
# final_list_start = changes['should_be'].tolist()
#
# for elem in initial_list_start:
# 	initial_list.append(elem.encode('utf-8'))
# for elem in final_list_start:
# 	final_list.append(elem.encode('utf-8'))
#
#
#
#
# # 		read csv
# df2 = pd.read_csv('megapolis_print.csv', sep=';') #, encoding='utf-8'
# elem_name = df2['column'].tolist()
# elem_name = elem_name[6:30]		#[6:392]
# # print elem_name
#
#
# df = pd.DataFrame(output_list)
# print(df)
# # изменить на запись в csv
# # python dataframe pandas save to csv file format
# # file_writer = csv.writer(w_file, delimiter = "\t")
#
# file_output = 'output_' + str(random.randint(1,1000)) + '.xlsx'
# df.to_excel(file_output, 'Sheet1')
