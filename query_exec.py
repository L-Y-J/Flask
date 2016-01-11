#!usr/bin/env python
# -*- coding: utf-8 -*-

import db_accessor
from query_generator import QuerySql


def query_bug_list():
    return db_accessor.exec_sql(QuerySql('').query_patch())


if __name__ == '__main__':
    query_bug_list()
