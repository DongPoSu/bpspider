# coding=utf-8
import os
import platform
import sqlite3

# class SqliteContext:
#     def insert(self):
#         pass
#
#     def delete(self):
#         pass
#
#     def select(self):
#         pass



db_path = "D:\\python_work\\bpspider\dao\\account.db"


def select():
    conn = sqlite3.connect("account.db")
    cursor = conn.execute("SELECT * FROM single_select_subject")
    for row in cursor:
        print(row[0])
    conn.close()


def insert_single_test(data_list):
    conn = sqlite3.connect(db_path)
    sql = "insert into single_select_subject (test_id,content,right_answer,sort_index) VALUES (\'{testId}\',\'{contents}\',\'{right_answer}\',{sort_index})"
    for data in data_list:
        cursor = conn.execute(
            sql.format(testId=data.test_id, contents=data.content, right_answer=data.right_answer,
                       sort_index=data.sort_index))
        conn.commit()
    conn.close()


def insert_multi_test(data_list):
    conn = sqlite3.connect(db_path)
    sql = "insert into multi_select_subject (test_id,content,right_answer,sort_index) VALUES (\'{testId}\',\'{contents}\',\'{right_answer}\',{sort_index})"
    for data in data_list:
        cursor = conn.execute(
            sql.format(testId=data.test_id, contents=data.content, right_answer=data.right_answer,
                       sort_index=data.sort_index))
        conn.commit()
    conn.close()


def insert_judge_test(data_list):
    conn = sqlite3.connect(db_path)
    sql = "insert into judge_subject (test_id,content,right_answer,sort_index) VALUES (\'{testId}\',\'{contents}\',\'{right_answer}\',{sort_index})"
    for data in data_list:
        cursor = conn.execute(
            sql.format(testId=data.test_id, contents=data.content, right_answer=data.right_answer,
                       sort_index=data.sort_index))
        conn.commit()
    conn.close()


def insert_test(data_list):
    conn = sqlite3.connect(db_path)
    sql = "insert into test (test_id,test_name,catagory_id,type,sort_index) VALUES (\'{test_id}\',\'{test_name}\',\'{catagory_id}\',{type},{sort_index})"
    for data in data_list:
        cursor = conn.execute(
            sql.format(test_id=data.test_id, test_name=data.test_name, catagory_id=data.catagory_id,
                       type=data.type, sort_index=data.sort_index))
        conn.commit()
    conn.close()


def insert_calc_test(data_list):
    conn = sqlite3.connect(db_path)
    sql = "insert into calculation_subject (test_id,content,right_answer,sort_index) VALUES (\'{testId}\',\'{contents}\',\'{right_answer}\',{sort_index})"
    for data in data_list:
        cursor = conn.execute(
            sql.format(testId=data.test_id, contents=str(data.content), right_answer=str(data.right_answer),
                       sort_index=data.sort_index))
        conn.commit()
    conn.close()


def insert_practice_test(data_list):
    conn = sqlite3.connect(db_path)
    sql = "insert into practice_subject (test_id,content,right_answer,sort_index) VALUES (\'{testId}\',\'{contents}\',\'{right_answer}\',{sort_index})"
    for data in data_list:
        cursor = conn.execute(
            sql.format(testId=data.test_id, contents=str(data.content), right_answer=str(data.right_answer),
                       sort_index=data.sort_index))
        conn.commit()
    conn.close()
