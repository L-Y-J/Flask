#!usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request

import db_accessor
from query_generator import QuerySql, QueryCondition


def query_patch_list():
    s = request.args.get('startDate')
    e = request.args.get('endDate')
    c = QueryCondition(s, e)
    query_sql = QuerySql(c)
    return db_accessor.exec_sql(query_sql.query_patch_forlist(), query_sql.condition.condition_list)
