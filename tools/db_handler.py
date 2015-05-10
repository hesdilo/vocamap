# -*- coding: utf-8 -*-
'''
Created on 2015年4月23日

@author: dilo
'''

import os
import sqlite3
from config import DB_PATH, SQL_FILE

db_path     = DB_PATH()
sql_file    = SQL_FILE()

global g_connect

def init_db():
    # create empty database.
    if os.path.exists(db_path):
        os.remove(db_path)
    cn = sqlite3.connect(db_path)
    cu = cn.cursor()
    # read and execute SQL file.
    sql = open(sql_file)
    for line in sql:
        if not line.startswith('#'):
            cu.execute(line)
    # close database.
    cu.close()


def open_db():
    global g_connect
    if not locals().has_key('g_connect'):
        g_connect = sqlite3.connect(db_path)


def close_db():
    open_db()
    g_connect.close()


def add_similar(word1, word2, similarity):
    try:
        open_db()
        g_connect.execute('insert into similar values (?, ?, ?)', (word1, word2, similarity))
        g_connect.commit()
    except Exception:
        print word1, word2


def get_similar(word, similarity):
    words = {}
    open_db()
    cu = g_connect.cursor()
    cu.execute('select * from similar where similarity >= %d and word1 = "%s"' % (similarity, word))
    for i in cu.fetchall():
        words[i[1]] = i[2]
    cu.execute('select * from similar where similarity >= %d and word2 = "%s"' % (similarity, word))
    for i in cu.fetchall():
        words[i[0]] = i[2]
    return words


if __name__ == '__main__':
    init_db()
