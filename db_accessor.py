#!usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc


def exec_sql(sql):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.16.50.151;DATABASE=SDP2_NC;UID=SDPforlipy;PWD=SDPforlipy2012')
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchone()
    conn.close()
    return rows


if __name__ == '__main__':
    print 'start test...'
    print exec_sql('select * from cqmaster.t_supportwebquestion')