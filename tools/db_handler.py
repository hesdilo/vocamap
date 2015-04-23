# -*- coding: utf-8 -*-
'''
Created on 2015年4月23日

@author: dilo
'''

import sqlite3
from config import DB_PATH, SQL_FILE

db_path     = DB_PATH()
sql_file    = SQL_FILE()


def init_db():
    # open database.
    cn = sqlite3.connect(db_path)
    cu = cn.cursor()
    # read and execute SQL file.
    sql = open(sql_file)
    for line in sql:
        if not line.startswith('#'):
            cu.execute(line)
    # close database.
    cu.close()


if __name__ == '__main__':
    init_db()